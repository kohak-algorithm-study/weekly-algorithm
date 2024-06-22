
def binary_search(array, target, start, end):
    if start > end:  # 모든 탐색을 했는데, 원소를 못찾은 경우
        return None

    mid = (start + end) // 2  # 중간 인덱스
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, array[mid - 1])
    else:
        return binary_search(array, target, array[mid + 1], end)


n, target = map(int, input().split())
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result is None:
    print("원소가 존재하지 않습니다")
else:
    # 찾고자 하는 원소가 배열의 몇번째 원소인지 출력
    print(result + 1)
