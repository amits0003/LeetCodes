"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab"
are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any
permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_length = len(words[0])  # All words are of the same length
        total_length = word_length * len(words)  # Total length of concatenated words
        word_count = Counter(words)  # Count frequency of each word in `words`

        result = []

        # Loop over all possible starting points (0 to word_length - 1)
        for i in range(word_length):
            left = i
            current_count = Counter()
            for right in range(i, len(s) - word_length + 1, word_length):
                word = s[right:right + word_length]

                if word in word_count:
                    current_count[word] += 1

                    # If we have more of the word than expected, shift the window
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_length]] -= 1
                        left += word_length

                    # If the current window matches the length of concatenated words
                    if right - left + word_length == total_length:
                        result.append(left)
                else:
                    # If the word is not in `words`, reset the current window
                    current_count.clear()
                    left = right + word_length

        return result
