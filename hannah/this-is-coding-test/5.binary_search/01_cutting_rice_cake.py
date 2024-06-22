'''
참고) 파라메트릭 서치
파라메트릭 서치란 최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
- 최적화 문제란 어떤 함수의 값을 가능한 낮추거나 최대한 높이는 문제를 말한다.
- 이런 문제를 바로 해결하기가 어려운 경우 여러 번의 서정 문제를 이용해서 문제 형태를 바꾸어서 해결할 수 있는데, 이를 파라메터릭 서치 기법이라고 한다
- 예) 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 일반적으로 코테에서 파라메터릭 서치 문제가 나오면 이진 탐색을 이용해서 해결할 수 있다.

'''

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())  # n = 떡의 개수, m = 손님이 요청한 떡의 길이(최소한 이만큼 가져가야 함)
array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

# 이진탐색 시나리오
# 중간값(h)으로 떡을 자른다
# 잘린 떡들의 길이 합이 m보다 큰가?
# m과 같으면 탐색 종료
# m보다 크면 합을 줄일 수 있는지 확인 -> 현재 중간값을 기준으로 배열의 오른쪽 범위를 대상으로 이진탐색
# 작으면 이진탐색 -> 중간값을 줄인다 -> 현재 중간값을 기준으로 배열의 왼쪽 범위를 대상으로 이진탐색
# 최초로 m을 넘길때의 h를 구한다

# 최초 중간값 : 가장 긴 떡의 길이의 절반
# start: 0, end: 가장 긴 떡의 길이
start = 0
end = array[-1]
result = 0
while True:
    if start > end:
        break

    h = (start + end) // 2

    rest_sum = sum(map(lambda x: (x - h) if x >= h else 0, array))

    if rest_sum == m:
        result = h
        break

    elif rest_sum > m:
        start = h + 1
    else:
        end = h - 1

print(result)
