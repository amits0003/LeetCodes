import gc

i = 0

# # create a cycle and on each iteration x as a dictionary
# # assigned to 1
# def create_cycle():
#     x = {}
#     x[i + 1] = x
#     print(x)


# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect()  # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))

# print("Creating cycles...")
# for i in range(10):
#     create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))

""" arrange the list into descending using lambda functions"""

x = [1, 4, 44, 3, 4, 5, 6, 90, 12, 34, 56, 12, 54, 56, 67, 3]

sortedResult = sorted(x, key=lambda d: -d)
print(sortedResult)

y = [1, 4, 44, 3, 4, 5, 6, 90, 12, 34, 56, 12, 54, 56, 67, 3]
y.sort(key=lambda d: -d)
print(y)







