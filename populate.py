#
# Populate (ingest) a few items to simulate the ingestion process.
#

import sqlite3
import sys


def insert_db(items: list, date: str) -> None:
    """
    Insert 'items' in the DB.
    """

    conn = sqlite3.connect("r2p.db")
    cur = conn.cursor()

    for item in items:
        res = cur.execute("SELECT * FROM items WHERE item=?", (item,)).fetchall()
        if not len(res):
            print(f"New item '{item}'")
            cur.execute("INSERT INTO items VALUES(NULL, ?)", (item,))
        else:
            print(f"Duplicated item '{item}'")

        params = {"dt_ingest": date, "item": item}
        cur.execute(
            "INSERT INTO ingested (id, id_item, dt_ingest, is_verified) SELECT NULL, id, :dt_ingest,0 FROM items WHERE item = :item",
            params,
        )

    conn.commit()
    print(f"Total changes: '{conn.total_changes}'")


def read_sample_file(sample_file):
    """
    Read a file with sample items to test insertion into the db.
    """

    with open(sample_file, "r") as fin:
        text = fin.readlines()

    text = [line.strip() for line in text]

    return text


def main():
    sample_file = sys.argv[1]

    # Define some date in the past to test ingesting the item again
    # in a date in the future.
    ingest_date = sys.argv[2]

    # Read sample items file
    ingested_list = read_sample_file(sample_file)

    # ingested_list = ingested_list[:4]
    # print(ingested_list)

    insert_db(ingested_list, ingest_date)


if __name__ == "__main__":
    main()
