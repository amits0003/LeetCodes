import json


def print_directory(directory, prefix=''):
    name = directory['name']
    print(prefix + name)

    if 'contents' in directory:
        for item in directory['contents']:
            if 'contents' in item:
                print_directory(item, prefix + '  |-- ')
            else:
                print(prefix + '|-- ' + item['name'])


def main():
    with open('structure.json', 'r') as file:
        data = json.load(file)

    print_directory(data)


if __name__ == '__main__':
    main()

