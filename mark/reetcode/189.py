from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if k > len(nums):
            k = k % len(nums)

        copy_nums = nums[:len(nums) - k]

        for i in range(k):
            nums[i] = nums[len(nums) - k + i]

        for i in range(k, len(nums)):
            nums[i] = copy_nums[i - k]

        return nums


nums = [1,2,3,4,5,6,7]
print(Solution().rotate(nums, 3))