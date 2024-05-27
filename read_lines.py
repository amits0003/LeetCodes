def filter_lines_with_keyword(filename, keyword):
    filtered_lines = []
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                filtered_lines.append(line)
    return filtered_lines


filename = "data.txt"  # Replace 'example.txt' with your file name
keyword = "COCHEUCAD1357MH"
filtered_lines = filter_lines_with_keyword(filename, keyword)

print("Lines containing the keyword 'hellp':")
for line in filtered_lines:
    print(line.strip())
