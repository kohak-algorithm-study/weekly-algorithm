import itertools
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort(key=len)
        data = []
        shortest_str_char = ""

        for i in strs[0]:
            shortest_str_char = shortest_str_char+i
            data.append(shortest_str_char)

        result = []
        result.append(0)

        for i in range(1, len(data)):
            cnt = 0
            for j in range(1, len(strs)):
                if data[i] in strs[j]:
                    cnt += 1

            result.append(cnt)


        if result.index(max(result)) == 0:
            return ""
        else:
            return data[result.index(max(result))]




strs =  ["a"]
print(Solution().longestCommonPrefix(strs))