from itertools import permutations, combinations
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()  # 배열을 정렬합니다.
        result = set()
        seen = set()

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                complements = set()
                for j in range(i + 1, len(nums)):
                    complement = -nums[i] - nums[j]
                    if complement in complements:
                        result.add(tuple(sorted((nums[i], nums[j], complement))))
                    complements.add(nums[j])

        return [list(triplet) for triplet in result]


nums = [0,0,0]

print(Solution().threeSum(nums))
