'''
[정렬된 배열에서 특정 수의 개수 구하기]
N
'''
import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))


def binary_search(array, target, start, end):
    result = -1

    while True:
        if start > end:
            break

        mid = (start + end) // 2

        if array[mid] == x:
            result = mid
            break

        elif array[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return result


first_found_index = binary_search(array, x, 0, n)
