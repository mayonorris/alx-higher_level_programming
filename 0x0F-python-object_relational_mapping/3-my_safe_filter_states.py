#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, using safe parameterized queries.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    db = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})

    rows = cursor.fetchall()

    for row in rows:
        print(row)
