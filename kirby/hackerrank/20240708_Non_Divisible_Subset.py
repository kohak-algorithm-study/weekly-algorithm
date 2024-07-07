# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true
# Difficulty: Medium
import os
from collections import defaultdict


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    # Write your code here
    max_length = 0
    remain_count_map = defaultdict(int)
    for number in s:
        remain_count_map[number % k] += 1

    print(remain_count_map)
    if remain_count_map[0] >= 1:
        max_length += 1

    if k % 2 == 0:
        for i in range(1, k // 2):
            pair1 = remain_count_map[i]
            pair2 = remain_count_map[k-i]
            max_length += max(pair1, pair2)
            print('i', i, 'pair1', pair1, 'pair2', pair2, 'max_length', max_length)
        max_length += 1
    else:
        for i in range(1, (k // 2) + 1):
            pair1 = remain_count_map[i]
            pair2 = remain_count_map[k-i]
            max_length += max(pair1, pair2)
            print('i', i, 'pair1', pair1, 'pair2', pair2, 'max_length', max_length)

    return max_length


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    fptr.write(str(result) + '\n')
    fptr.close()
