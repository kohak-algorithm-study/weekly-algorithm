from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):

            dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)


#nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]
# nums = [-1]
print(Solution().maxSubArray(nums))
