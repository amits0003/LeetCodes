import json
import os
import sys
import argparse
from datetime import datetime

def list_directory_contents(contents, show_all=False):
    items = []
    for item in contents:
        if show_all or not item['name'].startswith('.'):
            items.append(item)
    return items

def format_item(item):
    permissions = item.get('permissions', '----------')
    size = item.get('size', 0)
    timestamp = item.get('time_modified', 0)
    date_time = datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')
    name = item['name']
    return f"{permissions} {size:>5} {date_time} {name}"

def filter_items(items, filter_option):
    if filter_option == "file":
        return [item for item in items if 'contents' not in item]
    elif filter_option == "dir":
        return [item for item in items if 'contents' in item]
    else:
        print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='List directory contents from JSON structure.')
    parser.add_argument('-A', action='store_true', help='Include all files and directories, including those starting with a dot')
    parser.add_argument('-l', action='store_true', help='List in long format with additional information')
    parser.add_argument('-r', action='store_true', help='Reverse the order of the output')
    parser.add_argument('-t', action='store_true', help='Sort by time modified')
    parser.add_argument('--filter', type=str, help='Filter the results by file or dir')
    args = parser.parse_args()

    json_file_path = 'structure.json'

    if not os.path.exists(json_file_path):
        print(f"Error: JSON file '{json_file_path}' not found.")
        sys.exit(1)

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    if 'contents' not in data:
        print("Error: Invalid JSON structure. 'contents' key not found.")
        sys.exit(1)

    top_level_contents = list_directory_contents(data['contents'], show_all=args.A)

    if args.t:
        top_level_contents.sort(key=lambda item: item.get('time_modified', 0))

    if args.r:
        top_level_contents.reverse()

    if args.filter:
        top_level_contents = filter_items(top_level_contents, args.filter)

    if args.l:
        for item in top_level_contents:
            print(format_item(item))
    else:
        print(' '.join([item['name'] for item in top_level_contents]))

if __name__ == '__main__':
    main()
