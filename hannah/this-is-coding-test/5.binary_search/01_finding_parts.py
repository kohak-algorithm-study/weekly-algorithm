import sys

n = int(input())
parts = list(map(int, sys.stdin.readline().split()))
m = int(input())
requests = list(map(int, sys.stdin.readline().split()))

parts.sort()


def binary_search(array, target, start, end):
    while True:
        if start > end:
            return False

        mid = (start + end) // 2

        if array[mid] == target:
            return True

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1


for i in requests:
    result = binary_search(parts, i, 0, n - 1)
    if result:
        print('yes', end=' ')
    else:
        print('no', end=' ')
