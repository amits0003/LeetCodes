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


def format_item(item, path_prefix=""):
    permissions = item.get('permissions', '----------')
    size = item.get('size', 0)
    timestamp = item.get('time_modified', 0)
    date_time = datetime.fromtimestamp(timestamp).strftime('%b %d %H:%M')
    name = os.path.join(path_prefix, item['name']) if path_prefix else item['name']
    return f"{permissions} {size:>5} {date_time} {name}"


def filter_items(items, filter_option):
    if filter_option == "file":
        return [item for item in items if 'contents' not in item]
    elif filter_option == "dir":
        return [item for item in items if 'contents' in item]
    else:
        print(f"error: '{filter_option}' is not a valid filter criteria. Available filters are 'dir' and 'file'.")
        sys.exit(1)


def find_path(data, path_parts):
    current_level = data
    for part in path_parts:
        if 'contents' in current_level:
            found = False
            for item in current_level['contents']:
                if item['name'] == part:
                    current_level = item
                    found = True
                    break
            if not found:
                print(f"error: cannot access '{'/'.join(path_parts)}': No such file or directory")
                sys.exit(1)
        else:
            if current_level['name'] == part:
                return current_level, '/'.join(path_parts[:-1])
            else:
                print(f"error: cannot access '{'/'.join(path_parts)}': No such file or directory")
                sys.exit(1)
    return current_level, '/'.join(path_parts)


def main():
    parser = argparse.ArgumentParser(description='List directory contents from JSON structure.')
    parser.add_argument('-A', action='store_true',
                        help='Include all files and directories, including those starting with a dot')
    parser.add_argument('-l', action='store_true', help='List in long format with additional information')
    parser.add_argument('-r', action='store_true', help='Reverse the order of the output')
    parser.add_argument('-t', action='store_true', help='Sort by time modified')
    parser.add_argument('--filter', type=str, help='Filter the results by file or dir')
    parser.add_argument('path', nargs='?', default='.', help='Path to the directory or file within the JSON structure')
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

    path_parts = args.path.split('/')
    target, path_prefix = find_path(data, path_parts)

    if 'contents' in target:
        items = list_directory_contents(target['contents'], show_all=args.A)

        if args.t:
            items.sort(key=lambda item: item.get('time_modified', 0))

        if args.r:
            items.reverse()

        if args.filter:
            items = filter_items(items, args.filter)

        if args.l:
            for item in items:
                print(format_item(item, path_prefix))
        else:
            print(' '.join([item['name'] for item in items]))
    else:
        if args.l:
            print(format_item(target, path_prefix))
        else:
            print(target['name'])


if __name__ == '__main__':
    main()
