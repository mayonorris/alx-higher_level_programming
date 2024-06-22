#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def list_cities(username, password, database):
    """Lists all cities from the database hbtn_0e_4_usa."""
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the query
        cursor.execute("SELECT cities.id, cities.name, states.name \
                        FROM cities \
                        INNER JOIN states ON cities.state_id = states.id \
                        ORDER BY cities.id ASC")

        # Fetch all rows
        cities = cursor.fetchall()

        # Display results
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        # Close cursor and database connection
        cursor.close()
        db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
