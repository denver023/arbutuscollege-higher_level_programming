#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa,
sorted by cities.id. It takes 3 arguments: mysql username, mysql
password, and database name.
"""

import MySQLdb
import sys


def list_cities_by_state():
    """Connect to MySQL, execute the query, and display the results."""

    # Ensure we have the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> "
              "<mysql password> <database name>")
        return

    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_password, db=database)

    # Create a cursor to execute the query
    cursor = db.cursor()

    # SQL query to fetch cities along with their state names
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    # Execute the query
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Print each result
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


# Ensure the script only runs when executed directly, not when imported
if __name__ == "__main__":
    list_cities_by_state()
