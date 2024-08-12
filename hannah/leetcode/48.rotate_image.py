'''
https://leetcode.com/problems/rotate-image/
'''

import copy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        copy_matrix = copy.deepcopy(matrix)

        for row, nums in enumerate(copy_matrix):
            print(f'가로: {row}')
            print(nums)
            for col, x in enumerate(nums):
                print(f'세로: {col}')
                matrix[col][n - row - 1] = x

        print(matrix)


solution = Solution()
solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
