'''
https://leetcode.com/problems/3sum/description/
'''

# 투포인터 사용
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) != 0:
            return []

        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        nums.sort()
        result = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))  # set의 요소들은 hashable 해야하는데, hashable 하려면 immutable 해야 함
                    left += 1
                    # right -= 1 로 해도 가능

        return [list(x) for x in result]
