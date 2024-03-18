#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument, using safe parameterized queries.
"""

import MySQLdb
import sys

def filter_states(username, password, database, state_name):
    """Displays all values in the states table where name matches the provided argument."""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database, state_name)
