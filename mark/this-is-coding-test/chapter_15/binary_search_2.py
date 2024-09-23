import sys



def binary_search(arr, fixed_point, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == fixed_point:
        return mid
    elif arr[mid] > fixed_point:
        return binary_search(arr, fixed_point, start, mid - 1)
    else:
        return binary_search(arr, fixed_point, mid + 1, end)



fixed_point = int(input())
a = list(map(int, sys.stdin.readline().split()))

index = binary_search(a, fixed_point, 0 , fixed_point-1)

if index == None:
    print(-1)
else:
    print(index)

