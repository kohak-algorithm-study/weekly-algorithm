'''
참고) 파이썬 이진 탐색 라이브러리: bisect
- bisect_left(array, target): 정렬된 순서를 유지하면서 배열 array에 target을 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(array, target): 정렬된 순서를 유지하면서 배열 array에 target을 삽입할 가장 오른쪽 인덱스를 반환

'''
# 값이 특정 범위에 속하는 데이터 개수 구하기

from bisect import bisect_left, bisect_right


def count_by_range(array, min_value, max_value):
    right_index = bisect_right(array, max_value)
    left_index = bisect_left(array, min_value)
    return right_index - left_index


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 구하기
print(count_by_range(a, 4, 4))  # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 구하기
print(count_by_range(a, -1, 3))  # 6
