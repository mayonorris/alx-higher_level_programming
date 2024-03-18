#!/usr/bin/python3
"""
This script retrieves states with names
beginning with the letter 'N' from the
specified MySQL database.
"""

import MySQLdb as db
from sys import argv

"""
Establishes a connection to the MySQL database
and fetches states starting with 'N'.
"""

if __name__ == '__main__':
    try:
        connection = db.connect(host="localhost", port=3306,
                                user=argv[1], passwd=argv[2], db=argv[3])
        cursor = connection.cursor()

        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
        cursor.execute(query)

        selected_rows = cursor.fetchall()

        for row in selected_rows:
            print(row)
            
    except Exception as e:
        print("An error occurred:", e)
    finally:
        cursor.close()
        connection.close()
