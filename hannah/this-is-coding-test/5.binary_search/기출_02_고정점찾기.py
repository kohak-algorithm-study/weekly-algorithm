'''
고정점이란, 수열의 원소 중에서 그 값이 인덱스와 동일한 원소를 의미합니다.
예를 들어 수열 a = {-15, —4, 2, 8, 13}이 있을 때 a[2] = 2 이므로, 고정점은 2가 됩니다.
하나의 수열이 N개의 서로 다른 원소를 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 고정점이 있다면, 고정점을 출력하는 프로그램을 작성하세요.
만약 고정점이 없다면 -1을 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 ‘시간 초과’ 판정을 받습니다.
'''
n = int(input())
array = list(map(int, input().split()))

start, end = 0, n - 1
result = -1
while start <= end:
    mid = (start + end) // 2

    if mid == array[mid]:
        result = mid
        break
    elif mid < array[mid]:
        end = mid - 1
    else:
        start = mid + 1

print(result)
