"""
input = [1, 2, 3, [4, 5, [6, 7, [8, 9 ], 10], 11], 12]
output = [1,2,3,4,5,6,7,8,9,10,11,12]
"""

inputList = [1, 2, 3, [4, 5, [6, 7, [8, 9], 10], 11], 12]
#outputList = [1,2,3,4,5,6,7,8,9,10,11,12]


tempList = []


def createListFromNestedList(inputList):
    outputList = []
    for k in inputList:
        if type(k) == list:
            createListFromNestedList(k)
        else:
            tempList.append(k)

    outputList = outputList + tempList

    return outputList


#PAF
# print(createListFromNestedList(inputList))

input_string = "aabbbccccaaaaa"
# output = "a2b3c4a5"
output = ""
count = 1
temp = []

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        temp.append(f"{input_string[i-1]}{count}")
        count = 1

temp.append(f"{input_string[-1]}{count}")

output = "".join(temp)

print(output)

