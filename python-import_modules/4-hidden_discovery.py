#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Retrieve all names defined in the module
    names = dir(hidden_4)
    # Filter names that do not start with "__" and sort alphabetically
    filtered_names = [name for name in names if not name.startswith("__")]
    # Print each name on a new line
    for name in sorted(filtered_names):
        print(name)
