"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern
 and a non-empty word in s. Specifically:
Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat".

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordList = s.split()

        char_to_word = {}
        word_to_char = {}

        if len(pattern) != len(wordList):
            return False

        for c, w in zip(pattern, wordList):
            if c in char_to_word:
                if char_to_word[c] != w:
                    return False
            if w in word_to_char:
                if word_to_char[w] != c:
                    return False

            char_to_word[c] = w
            word_to_char[w] = c

        return True


pattern1 = "abba"
s1 = "dog cat cat dog"
obj1 = Solution()
print(obj1.wordPattern(pattern1, s1))
