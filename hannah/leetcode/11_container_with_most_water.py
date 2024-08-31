'''
https://leetcode.com/problems/container-with-most-water/description/
'''
from typing import List


class Solution:
    def maxArea1(self, height: List[int]) -> int:
        n = len(height)
        max_area = 0
        for start in range(n - 1):
            sub_max_area = 0
            for end in range(start + 1, n):
                area = (end - start) * min(height[start], height[end])
                if area > sub_max_area:
                    sub_max_area = area

            if sub_max_area > max_area:
                max_area = sub_max_area
        return max_area

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = (end - start) * min(height[start], height[end])
            if area > max_area:
                max_area = area

            # 높이가 더 짧은 포인터를 갱신하여 현재 max_area보다 더 큰 값이 나올 수 있는지 탐색한다.
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return max_area


solution = Solution()
result = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)
