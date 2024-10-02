def find_pattern(arr):
    if len(arr) == 0:
        return []

    # Sort the array in ascending order
    arr.sort()

    result = []
    start = 0
    end = len(arr) - 1

    while start <= end:
        if end >= start:
            result.append(arr[end])  # Add max value
            end -= 1
        if start <= end:
            result.append(arr[start])  # Add min value
            start += 1

    return result


arr = [3,42, 5, 41, 44, 24, 64]
result = find_pattern(arr)
print(result)  # Output: [6, 1, 5, 2, 4, 3]
