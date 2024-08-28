'''
[정렬된 배열에서 특정 수의 개수 구하기]
N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다.
이때 이 수열에서 X가 등장하는 횟수를 계산하세요.
예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 X = 2 라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 ‘시간 초과’ 판정을 받습니다.
'''

n, x = map(int, input().split())
ordered_list = list(map(int, input().split()))


def find_first(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            result = mid
            end = mid - 1  # 다음 탐색 범위는 앞쪽
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return result


def find_last(array, target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            result = mid
            start = mid + 1  # 다음 탐색 범위는 뒤쪽
        elif array[mid] < target:
            end = mid - 1
        else:
            start = mid + 1

    return result


first_index = find_first(ordered_list, x, 0, n - 1)
if first_index == -1:
    print(-1)
else:
    last_index = find_last(ordered_list, x, 0, n - 1)
    print(last_index - first_index + 1)
