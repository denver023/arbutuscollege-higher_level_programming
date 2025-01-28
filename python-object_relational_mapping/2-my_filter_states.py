#!/usr/bin/python3
"""
Script that filters states by user input.
"""

import MySQLdb
import sys

def main():
    """Main entry point of the script."""
    # Check if the script is being executed directly
    if len(sys.argv) != 5:
        return

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    # Create and execute the query using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Fetch all results and print them
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main() 
