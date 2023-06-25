# 
# Populate (ingest) a few items to simulate the ingestion process.
#

import sqlite3

def insert_db(items:list, date:str) -> None:
    """Insert 'items' in the DB."""

    conn = sqlite3.connect('r2p.db')
    cur = conn.cursor()

    for item in items:
        sql_line = f"INSERT INTO items VALUES(NULL, '{item})'"
        cur.execute(sql_line)


def read_sample_file(sample_file):
    """
    Read a file with sample items to test insertion into the db.
    """

    with open(sample_file, 'r') as fin:
        text = fin.readlines()

    text = [line.strip() for line in text]

    return text

def main():
    sample_file = 'sample_items.txt'

    # Define some date in the past to test ingesting the item again
    # in a date in the future.
    ingest_date = "2023-06-10"

    # Read sample items file
    ingested_list = read_sample_file(sample_file)

    # print(ingested_list)

    insert_db(ingested_list, ingest_date)
    

if __name__ == "__main__":
    main()