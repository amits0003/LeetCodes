# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
"""create a generic function to find sum of all the numbers in nested list."""

ip = [5, 2, [4, [7, 5], [2, 1]], 1, 2, 3]


def sum_elements(ls):
    res = 0
    for ele in ls:
        if isinstance(ele, list):
            res += sum_elements(ele)
        else:
            res = res + ele
    return res


print(sum_elements(ip))

print(sum_elements([5, 2, [4, [], [2, 1]], 1, 2, 3]))

print(sum_elements([5, 2, [4, [0], [2, 1]], 1, 2, 3]))

print(sum_elements([5, 2, [4, [-2, 0], [2, 1]], 1, 2, 3]))

print(sum_elements([[5, 2, [4, [], [2, 1]], 1, 2, 3], [4, 4, 5]]))


