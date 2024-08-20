'''
https://leetcode.com/problems/first-unique-character-in-a-string/description/
'''


class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     from collections import deque

    #     hash_map = {}
    #     queue = deque()

    #     for i, x in enumerate(s):
    #         if hash_map.get(x) == None:
    #             hash_map[x] = 1
    #             queue.append((x))
    #         else:
    #             a = queue.popleft()
    #             return list(s).index(a)
    #     else:
    #         return -1

    def firstUniqChar(self, s: str) -> int:
        from collections import Counter

        counter = Counter(s)
        for i, x in enumerate(s):
            if counter[x] == 1:
                return i
        else:
            return -1


s = Solution()
result = s.firstUniqChar("leetcode")
print(result)
