import json


def print_directory_contents(contents, indent=0):
    for item in contents:
        # Determine the prefix based on the indentation level
        if indent > 0:
            prefix = '|' + '    ' * (indent - 1) + '|-- '
        else:
            prefix = '|-- ' if indent == 0 else ''
        print(f"{prefix}{item['name']}")
        # If the item is a directory, recursively print its contents
        if 'contents' in item:
            print_directory_contents(item['contents'], indent + 2)


def main():
    # Load the JSON data from the file
    with open('structure.json', 'r') as file:
        data = json.load(file)

    # Print the root directory
    print(data['name'])

    # Print the contents of the root directory
    if 'contents' in data:
        print_directory_contents(data['contents'], indent=0)


if __name__ == '__main__':
    main()
