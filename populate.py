# 
# Populate (ingest) a few items to simulate the ingestion process.
#

import sqlite3

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

    print(ingested_list)

    

if __name__ == "__main__":
    main()