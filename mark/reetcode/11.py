from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        areas = []
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                height_min = min(height[i], height[j])
                area = width * height_min
                areas.append(area)

        print(max(areas))




height = [1,8,6,2,5,4,8,3,7]
Solution().maxArea(height)