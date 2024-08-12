from copy import deepcopy
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)
        m = len(matrix[0])

        rotate_matrix = deepcopy(matrix)

        for i in range(n):
            for j in range(m):
                matrix[j][n-1-i] = rotate_matrix[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(matrix)