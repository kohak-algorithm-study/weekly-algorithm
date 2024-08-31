'''
https://leetcode.com/problems/longest-common-prefix/description/
'''


class Solution:
    def longestCommonPrefix(self, strs) -> str:

        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        min_length = min(map(len, strs))
        prefix = ''
        for i in range(min_length):
            for j in range(1, len(strs)):
                if strs[j - 1][i] != strs[j][i]:
                    return prefix
            prefix += strs[0][i]

        return prefix

    def longestCommonPrefix2(self, strs) -> str:

        if len(strs) == 0:
            return ''

        if len(strs) == 1:
            return strs[0]

        strs.sort()  # 사전순으로 정렬
        first_str = strs[0]
        last_str = strs[-1]

        # 사전순으로 정렬하면 맨 첫 단어와 마지막 단어가 달라지는 지점 전까지가 공통된 문자열이라는 것을 알 수 있다
        prefix = ''
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] != last_str[i]:
                break
            prefix += first_str[i]

        return prefix


solution = Solution()
solution.longestCommonPrefix(["flower", "flow", "flight"])
