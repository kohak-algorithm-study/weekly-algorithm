# https://leetcode.com/problems/3sum-closest/description/
# Difficulty : Medium
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_diff = int(1e9)
        closest_sum = int(1e9)

        for i in range(len(nums) - 2):
            start_index = i + 1
            end_index = len(nums) - 1

            while start_index < end_index:
                local_sum = nums[i] + nums[start_index] + nums[end_index]

                if local_sum == target:
                    return target
                elif abs(target - local_sum) < min_diff:
                    min_diff = abs(target - local_sum)
                    closest_sum = local_sum

                if local_sum > target:
                    end_index -= 1
                else:
                    start_index += 1

        return closest_sum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))  # 2
print(Solution().threeSumClosest([0, 0, 0], 1))  # 0
