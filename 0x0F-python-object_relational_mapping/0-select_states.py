#!/usr/bin/python3
"""Script to select all states from database `hbtn_0e_0_usa`"""


if __name__ == "__main__":
    import MySQLdb
    import sys

    database = MySQLdb.connect(username = sys.argv[1],
            password = sys.argv[2],
            database_name = sys.argv[3])

    cur = database.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

