def check_palindrome(num):
    temp = str(num)
    print(temp[::-1])

    if temp == temp[::-1]:
        return True


def palindrome_chain_length(num: int) -> int:
    # pass
    if num < 0:
        return -1

    if num == 0:
        return 0

    counter = 0

    while not check_palindrome(num):
        temp = int(str(num)[::-1])
        num = num + temp
        counter = counter + 1

    return counter


print(palindrome_chain_length(87))