'''
https://leetcode.com/problems/maximum-subarray/description/
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n  # dp[n] = 인덱스 n까지의 최대 합
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)

    def maxSubArray2(self, nums: List[int]) -> int:
        maxsub = nums[0]
        temp_sum = 0
        for num in nums:
            if num < 0:
                temp_sum = 0
            temp_sum += num
