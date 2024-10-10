"""
Merge Sort is another classic example of a
divide and conquer algorithm. It involves dividing an array into two halves, sorting each half,
and then merging the sorted halves.
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example usage:
unsorted_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(unsorted_array)
print("Sorted Array:", sorted_array)

print(unsorted_array.sort(reverse=False))
