# for i in range(10):
#     for j in range(10):
#         print(j)
#     print("\n")
#     print(i)


n = 5
matrix = [[(i * n) + j + 1 for j in range(n)] for i in range(n)]

for row in matrix:
    print(row)

