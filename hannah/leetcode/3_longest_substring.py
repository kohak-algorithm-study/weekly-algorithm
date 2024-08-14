# 투포인터 알고리즘 사용

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        s = list(s)
        n = len(s)

        # sub string의 길이가 set으로 했을 때의 길이와 같지 않을 때 까지 end += 1
        # 길이가 같으면 max_len 갱신
        # 길이가 같지 않아질 때 start += 1
        end = 0
        for start in range(n):
            while True:
                sub_str = s[start: end + 1]
                if len(sub_str) != len(set(sub_str)) or end == n:
                    break
                end += 1

                if len(sub_str) > max_len:
                    max_len = len(sub_str)

        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        max_len = 0
        sub_str = ''
        for i in range(len(s)):
            if s[i] not in sub_str:
                sub_str += s[i]
            else:
                # 이미 있는거라면 중복되는 문자가 나올때까지 맨 앞글자 자르고 sub_str 초기화
                while s[i] in sub_str:
                    sub_str = sub_str[1:]
                # 중복된 문자열을 없앤 다음에 이번 문자를 뒤에 붙여줌
                sub_str += s[i]

            if len(sub_str) > max_len:
                max_len = len(sub_str)

        return max_len


solution = Solution()
result = solution.lengthOfLongestSubstring3("abcabcbb")
print(result)
