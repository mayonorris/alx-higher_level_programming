#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

def filter_cities(username, password, database, state_name):
    """Lists all cities of the given state from the database hbtn_0e_4_usa."""
    try:
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()

        if cities:
            cities_str = ', '.join(city[0] for city in cities)
            print(cities_str)

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

    filter_cities(username, password, database, state_name)
