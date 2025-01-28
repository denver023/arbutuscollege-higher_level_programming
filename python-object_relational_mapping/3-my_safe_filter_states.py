#!/usr/bin/python3
"""
Script that takes in 4 arguments (mysql username, mysql password,
database name, and state name) and displays all values in the states table
where name matches the argument. It is safe from SQL injection.
"""

import MySQLdb
import sys


def safe_filter_states():
    """Connect to MySQL, execute a safe query, and display the results."""

    # Ensure we have the correct number of arguments
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql username> "
              "<mysql password> <database name> <state name>")
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

    # Use a parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the parameterized value
    cursor.execute(query, (state_name,))

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
    safe_filter_states()
