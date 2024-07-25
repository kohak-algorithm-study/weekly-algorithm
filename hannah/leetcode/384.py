import random
from copy import deepcopy
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums

    def reset(self) -> List[int]:
        return self.origin

    def shuffle(self) -> List[int]:
        nums = deepcopy(self.origin)
        random.shuffle(nums)
        return nums


solution = Solution([1, 2, 3])
result = solution.shuffle()
print(result)
result = solution.reset()
print(result)
result = solution.shuffle()
print(result)
