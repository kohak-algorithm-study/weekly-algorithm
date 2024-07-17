import random
from typing import List


class Solution:
    origin_nums = List[int]
    nums = List[int]

    def __init__(self, nums: List[int]):
        self.origin_nums = nums.copy()
        self.nums = nums

    def reset(self) -> List[int]:
        return self.origin_nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums
