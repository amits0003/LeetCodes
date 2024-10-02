

def pallindrome(x):
    if x >= 0:
        sign = 1
    else:
        return False
    temp = abs(x)
    rev_x = 0
    while temp != 0:
        rem = temp%10
        rev_x = rev_x*10 + rem
        temp = temp // 10

    rev_x = rev_x * sign
    if x == rev_x:
        return True
    else:
        return False


print(pallindrome(-121))

signedChar = str(-121)
