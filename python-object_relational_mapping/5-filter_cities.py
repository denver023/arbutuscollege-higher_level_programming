#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create cursor object
        cursor = db.cursor()

        # Create SQL query with parameter placeholder
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """

        # Execute query with parameterized value
        cursor.execute(query, (state_name,))

        # Fetch all results
        results = cursor.fetchall()

        # Print cities separated by commas
        cities = [city[0] for city in results]
        print(", ".join(cities))

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        sys.exit(1)
