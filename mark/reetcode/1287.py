from collections import Counter
from typing import List


class Solution:
    def findSpecialInteger(arr: List[int]) -> int:

        arr_count = Counter(arr)
        return (int(arr_count.most_common(n=1)[0][0]))


arr = [1,2,2,6,6,6,6,7,10]
print (Solution.findSpecialInteger(arr))

'''
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/submissions/1320539685/
'''