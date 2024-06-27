import json
import os
import sys
import argparse
from datetime import datetime


def list_directory_contents(contents, show_all=False):
    items = []
    for item in contents:
        # Include all items if show_all is True, otherwise omit items that start with a dot
        if show_all or not item['name'].startswith('.'):
            items.append(item)
    return items


def format_item(item):
    # Permissions
    permissions = item.get('permissions', '----------')
    # Size
    size = item.get('size', 0)
    # Time modified
    timestamp = item.get('time_modified', 0)
    date_time = datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')
    # Name
    name = item['name']
    return f"{permissions} {size:>5} {date_time} {name}"


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='List directory contents from JSON structure.')
    parser.add_argument('-A', action='store_true',
                        help='Include all files and directories, including those starting with a dot')
    parser.add_argument('-l', action='store_true', help='List in long format with additional information')
    parser.add_argument('-r', action='store_true', help='Reverse the order of the output')
    args = parser.parse_args()

    # Define the path to the JSON file
    json_file_path = 'structure.json'

    # Load the JSON data from the file
    if not os.path.exists(json_file_path):
        print(f"Error: JSON file '{json_file_path}' not found.")
        sys.exit(1)

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Ensure the data contains the expected structure
    if 'contents' not in data:
        print("Error: Invalid JSON structure. 'contents' key not found.")
        sys.exit(1)

    # List the top-level directory contents
    top_level_contents = list_directory_contents(data['contents'], show_all=args.A)

    # Reverse the order if -r is specified
    if args.r:
        top_level_contents.reverse()

    # Print the results
    if args.l:
        for item in top_level_contents:
            print(format_item(item))
    else:
        print(' '.join([item['name'] for item in top_level_contents]))


if __name__ == '__main__':
    main()
