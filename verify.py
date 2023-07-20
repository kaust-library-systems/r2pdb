#
# Simulate the verification of SHA1 of the ingested items.
#

import sqlite3
import sys
from collections import namedtuple


def verify_item(verify_date:str) -> None:
    """
    Verify the checksum SHA1 of ingested items.
    """

    conn = sqlite3.connect("r2p.db")
    cur = conn.cursor()

    #
    # Check items that were ingested but not verified, or that were ingested again.
    res = cur.execute("SELECT * FROM ingested WHERE is_verified=FALSE").fetchall()
    ingested_item = namedtuple(
        "i_item", ["id", "id_item", "date_ingested", "is_verified"]
    )

    for ii in map(ingested_item._make, res):
        vv = {"id": None, "id_item": ii.id_item, "dt_verified": verify_date}
        cur.execute(
            "INSERT INTO verified (id, id_item, dt_verify) VALUES(NULL, :id_item, :dt_verified)",
            vv,
        )
        cur.execute("UPDATE ingested SET is_verified = 1 WHERE id_item = :id_item", vv)

    conn.commit()
    print(f"Total changes: '{conn.total_changes}'")


def main() -> None:
    verify_date = sys.argv[1]

    verify_item(verify_date)


if __name__ == "__main__":
    main()
