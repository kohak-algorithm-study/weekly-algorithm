from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        dp = [0] * len(prices)

        for i in range(1, len(prices)):
            dp[i] = dp[i-1] + max(0, prices[i] - prices[i-1])

        return dp[-1]



prices = [7,1,5,3,6,4]
Solution().maxProfit(prices)