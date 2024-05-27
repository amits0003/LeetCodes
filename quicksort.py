zList = [1, 4, 44, 3, 4, 5, 6, 90, 12, 34, 56, 12, 54, 56, 67, 3]


def quicksortDescend(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    right = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]

    return quicksortDescend(left) + middle + quicksortDescend(right)


print("quick sort Descend")
zList = quicksortDescend(zList)
print(zList)

newlist = [1, 4, 44, 3, 4, 5, 6, 90, 12, 34, 56, 12, 54, 56, 67, 3]

ascendSort = lambda arr: arr if len(arr) <= 1 else ascendSort([x for x in arr[1:] if x < arr[0]]) + [
    arr[0]] + ascendSort([x for x in arr[1:] if x >= arr[0]])

descendSort = lambda arr1: arr1 if len(arr1) <= 1 else descendSort([x for x in arr1[1:] if x >= arr1[0]]) + [
    arr1[0]] + descendSort([x for x in arr1[1:] if x < arr1[0]])

newlist = ascendSort(newlist)

print("ascend Sort of List = ", newlist)

newlist = descendSort(newlist)

print("descend Sort of List = ", newlist)


def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


closure = outer_function(5)
print(closure(1))

newlist1 = [1, 4, 44, 3, 4, 5, 6, 90, 12, 34, 56, 12, 54, 56, 67, 3]
sorted_list = sorted(newlist1, reverse=True)

