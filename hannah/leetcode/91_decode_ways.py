class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        if s[0] != '0':
            dp[0] = 1

        if s[1] != '0':
            dp[1] = dp[0]

        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1

        for i in range(2, len(s)):
            if int(s[i]) != 0:
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 1: i + 1]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-2]


solution = Solution()

solution.numDecodings("11106")
