import os
import re

def search_files(regex_pattern):
    # os.path.expanduser("~") to get the path of the user's home directory.
    home_directory = os.path.expanduser("~")
    matching_files = []

    # Compile the regex pattern
    pattern = re.compile(regex_pattern)

    # Iterate over files in the home directory
    # os.walk() function walks through all the directories recursively.
    for root, dirs, files in os.walk(home_directory):
        for file in files:
            # Check if the filename matches the regex pattern
            if pattern.match(file):
                matching_files.append(os.path.join(root, file))

    return matching_files

if __name__ == "__main__":
    regex_pattern = input("Enter the regex pattern to search for files: ")
    matching_files = search_files(regex_pattern)

    if matching_files:
        print("Matching files:")
        for file in matching_files:
            print(file)
    else:
        print("No files matching the regex pattern found.")
