def second_largest(arr):
    # Ensure array has at least two elements
    if len(arr) < 2:
        return "Array should have at least two elements"

    largest = max(arr[0], arr[1])
    second_largest = min(arr[0], arr[1])

    for i in range(2, len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]

    return second_largest

# Example usage
arr = [12, 35, 1, 10, 34, 1]
# print("Second largest number:", second_largest(arr))

def secLargest(Arr):
    largest = max(Arr)
    arr.remove(largest)
    secLar = max(Arr)
    return secLar


print("Second largest number:", secLargest(arr))