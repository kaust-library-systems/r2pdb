#
# Create the database and tables from the SQL files.

import sqlite3

def read_sql(sql_file):
    """
    Read the content of a SQL file.
    """
    with open(sql_file,'r') as ff:
        text = ff.readlines()

    # Convert list to text
    command = ''.join([line.strip() for line in text])
    return command


def main():
    sql_tables = ['items.sql', 'verify.sql', 'ingest.sql']
    sql_db = 'r2p.db'

    con = sqlite3.connect(sql_db)

    cur = con.cursor()

    for tt in sql_tables:
        print(f"Creating table '{tt}'", end='... ')
        command = read_sql(tt)
        cur.execute(command)
        print('done')


if __name__ == "__main__":
    main()