from collections import deque
# from copy import copy
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # copy_nums = copy(nums)
        copy_nums = nums[:]  # 얕은 copy (위와 같음)

        if k > len(nums):
            k = k % len(nums)

        for i in range(len(nums)):
            nums[i] = copy_nums[i-k]

        print(nums)

    def rotate2(self, nums: List[int], k: int) -> None:
        q = deque(nums)
        q.rotate(k)
        new_list = list(q)

        for i in range(len(nums)):
            nums[i] = new_list[i]

        print(nums)


solution = Solution()
solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
