#!/usr/bin/python3
"""
Script that lists all states with name starting with N
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Lists all states with name starting with N from the database
    Args:
        username (str): MySQL username
        password (str): MySQL password
        db_name (str): Database name
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

    # Execute query to get states starting with N (case sensitive)
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all results
    states = cursor.fetchall()

    # Print results
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
