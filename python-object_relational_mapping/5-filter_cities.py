#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa,
sorted by cities.id. It takes 4 arguments: mysql username, mysql password,
database name, and state name.
"""

import MySQLdb
import sys


def filter_cities_by_state():
    """Connect to MySQL, execute the query, and display the results."""

    # Ensure we have the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password> "
              "<database name> <state name>")
        return

    # Get arguments from command line
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_password, db=database)

    # Create a cursor to execute the query
    cursor = db.cursor()

    # SQL query to fetch cities of a specific state, parameterized to prevent SQL injection
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the results
    results = cursor.fetchall()

    # Print the cities in the required format
    if results:
        print(", ".join([row[0] for row in results]))
    else:
        print()

    # Close the cursor and the database connection
    cursor.close()
    db.close()


# Ensure the script only runs when executed directly, not when imported
if __name__ == "__main__":
    filter_cities_by_state()
