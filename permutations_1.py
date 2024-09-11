def find_permutation(s, result):
    if len(s) == 0:
        print(result)
        return
    for j in range(len(s)):
        pivot = s[j]

        tempStr = s[:j] + s[j + 1:]

        find_permutation(tempStr, result + pivot)


string1 = "abcde"
# result = ""
find_permutation(string1, "")