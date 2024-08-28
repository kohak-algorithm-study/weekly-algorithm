'''
https://www.acmicpc.net/problem/2110
'''
import sys

input = sys.stdin.readline
n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()


def binary_search(c):
    if c == 2:
        return houses[-1] - houses[0]

    result = 0
    start, end = 1, houses[-1] - houses[0]  # 두 공유기 사이의 범위를 팀색 범위로 설정. 최소값=1, 최대값=(가장 끝 집과 가장 앞 집과의 거리)
    while start <= end:

        mid = (start + end) // 2

        current = houses[0]  # 맨 첫집에 무조건 공유기를 설치한다고 가정
        cnt = 1  # 설치한 공유기 개수
        for i in range(1, n):
            gap = houses[i] - current
            if gap >= mid:  # 둘 사이의 거리가 mid보다 크거나 같으면 설치
                current = houses[i]
                cnt += 1

        if cnt >= c:
            result = mid  # 공유기를 c개 설치했으면 일단 기록
            # 더 큰 값을 찾기 위해 다시 탐색 -> 범위 재설정 (현재 구한 mid보다 큰 값을 구하는게 목표이므로 start를 조절)
            start = mid + 1
        else:
            # 현재 mid보다 큰 gap으로는 공유기를 설치할 수 없다는 뜻이므로 mid를 줄인다
            end = mid - 1

    return result


result = binary_search(c)
print(result)
