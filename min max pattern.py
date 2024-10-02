# max, min pattern

inputData = [7, 8, 9, 6, 4, 5, 3, 44, 66, 67, 33, 33, 3434]


def max_min_pattern(data):
    outputPattern = []
    inputData.sort(reverse=True)

    print(inputData)

    lenIpData = len(inputData)

    mid_range_len = lenIpData // 2

    # print(mid_range_len)

    for each_num in range(mid_range_len):
        outputPattern.append(inputData[each_num])
        outputPattern.append(inputData[lenIpData - 1])
        lenIpData = lenIpData - 1

    for num in inputData:
        if num not in outputPattern:
            outputPattern.append(num)

    return outputPattern


op = max_min_pattern(inputData)
print(op)
