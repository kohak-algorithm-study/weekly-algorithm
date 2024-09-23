import sys


def count_by_value(arr, x):
    n = len(arr)

    a = first(arr, x,0 , n - 1)

    if a == None:
        return 0

    b = last(arr, x, 0 , n - 1)

    return b - a + 1

def first(arr, x, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
        return mid
    elif arr[mid] >= x:
        return first(arr, x, start, mid - 1)
    else:
        return first(arr, x, mid + 1, end)

def last(arr, x, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return last(arr, x, start, mid - 1)
    else:
        return last(arr, x, mid + 1, end)


n, x = map(int, sys.stdin.readline().rstrip().split())

x_list = list(map(int, sys.stdin.readline().split()))

count = count_by_value(x_list, x)

if count == 0:
    print(-1)
else:
    print(count)

# 7 2
# 1 1 2 2 2 2 3
