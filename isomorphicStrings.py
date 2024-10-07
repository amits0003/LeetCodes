"""Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Explanation:
The strings s and t can be made identical by:
Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:
Input: s = "foo", t = "bar"
Output: false
Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.
Example 3:
Input: s = "paper", t = "title"
Output: true"""

# Method 1 : some edge case are failing here

class Solution:
    def checkFreq(self, s):
        d = {}
        for ele in s:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1

        sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
        val_list = []
        for value in sorted_d.values():
            val_list.append(value)

        return val_list

    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = self.checkFreq(s)
        dict2 = self.checkFreq(t)

        return dict1 == dict2


s = "foo"
t = "bar"
obj1 = Solution()
print(obj1.isIsomorphic(s,t))

# Methdod 2 : creating character mapping

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Dictionaries to store the mapping
        map_s_to_t = {}
        map_t_to_s = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            # Check if there is an inconsistent mapping
            if (char_s in map_s_to_t and map_s_to_t[char_s] != char_t) or \
                    (char_t in map_t_to_s and map_t_to_s[char_t] != char_s):
                return False

            # Create the mapping between the characters
            map_s_to_t[char_s] = char_t
            map_t_to_s[char_t] = char_s

        return True


