class Solution:
    def firstUniqChar(self, s: str) -> int:

        dictionary = {}

        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1

        for i in range(len(s)):
            if dictionary[s[i]] == 1:
                return i

        return -1


s = "leetcode"
print(Solution().firstUniqChar(s))