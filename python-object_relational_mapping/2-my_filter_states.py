#!/usr/bin/python3
"""
Script that displays all values in the states table
where name matches the argument
"""
import MySQLdb
import sys


def filter_states_by_input(username, password, db_name, state_name):
    """
    Lists all states where name matches the argument
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Database name
        state_name (str): Name of state to search for
    """
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Create and execute query using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(state_name))

    # Fetch all results
    states = cursor.fetchall()

    # Print results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_input(sys.argv[1], sys.argv[2], 
                             sys.argv[3], sys.argv[4])
