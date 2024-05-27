"""Find the fibonacci Series of N Numbers"""


"""First Approach  : Normal Way : Recursion """


def fib_way1(n):
    if n <= 1:
        return n
    return fib_way1(n-1) + fib_way1(n-2)


#print(fib_way1(40))


"""Second Approach : using DP Memoization : Top-Bottom Approach : recursion depth is limited : approx 998 : above that :
stack will overflow"""


def fib_way2(m, s_dict={}):
    if m in s_dict:
        return s_dict[m]
    if m <= 1:
        s_dict[m] = m
    else:
        s_dict[m] = fib_way2(m-1, s_dict) + fib_way2(m-2, s_dict)

    return s_dict[m]


print(fib_way2(998))  # provide 999 and above to see the error

"""DP : 3rd Approach : using DP : Tabulation : bottom-up approach : recursion  depth is not limited. """


def fib_way3(n):
    if n <= 1:
        return n

    # Initialize the below table to store the fib series
    fib_table = [0] * (n + 1)
    fib_table[1] = 1

    #  iteration
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]

    return fib_table[n]


# Example usage:

result = fib_way3(10000) # you can provide any number of any limit to check the output of program
print(result)


"""fourth approach : without DP : where recursion depth is not limited"""


def fib(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


print(fib(10000))

