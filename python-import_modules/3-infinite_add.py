#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # Exclude the script name (sys.argv[0]) and cast arguments to integers
    arguments = map(int, sys.argv[1:])
    # Calculate the sum of the arguments
    result = sum(arguments)
    # Print the result followed by a new line
    print(result)
