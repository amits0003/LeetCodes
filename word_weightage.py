def char_value(c):
    return ord(c) - ord('a') + 1


def word_weightage(word):
    return len(word) * sum(char_value(c) for c in word)


l1 = ['abcd', 'bcdf', 'aaaa', 'bbbb']

sorted_l1 = sorted(l1, key=word_weightage)

print(sorted_l1)
