import sys
# loading gc
import gc

# get the current collection
# thresholds as a tuple
collected = gc.collect()

print("Garbage collector: collected",
          "%d objects." % collected)
# Create two objects that refer to each other
x = [1, 2, 3]
print(sys.getrefcount(x))
y = [4, 5, 6]
print(sys.getrefcount(x))
x.append(y)

print('x = ', x)
y.append(x)
print(sys.getrefcount(y))

print('y = ', y)

print('x1 = ', x)

print('y1 = ', y)

print(sys.getrefcount(x))# loading gc

print("Garbage collector: collected",
          "%d objects." % collected)