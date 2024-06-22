'''
[정렬된 배열에서 특정 수의 개수 구하기]
N
'''
import sys
from bisect import bisect_left, bisect_right

n, x = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

left_index = bisect_left(array, x)
right_index = bisect_right(array, x)

result = right_index - left_index
if result > 0:
    print(result)
else:
    print(-1)
