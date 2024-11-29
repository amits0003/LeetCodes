# Example 1: Basic use of id()
x = 10
y = 10
z = 20

print("ID of x:", id(x))  # Unique ID of x
print("ID of y:", id(y))  # Same ID as x because Python caches small integers
print("ID of z:", id(z))  # Different ID because z has a different value

# Example 2: Checking object identity
a = [1, 2, 3]
b = a  # b references the same list as a
c = a[:]  # c is a copy of the list

print("\nID of a:", id(a))
print("ID of b:", id(b))  # Same as a
print("ID of c:", id(c))  # Different because it's a copy

# Example 3: Verifying changes in identity
print("\nIDs before modification:")
print("ID of a:", id(a))

a.append(4)
print("\nIDs after modifying a:")
print("ID of a:", id(a))  # ID remains the same because the list is mutable

d = (1, 2, 3)  # Tuple (immutable object)
print("\nID of d before reassignment:", id(d))

d = (4, 5, 6)  # Reassignment creates a new object
print("ID of d after reassignment:", id(d))  # Different ID
