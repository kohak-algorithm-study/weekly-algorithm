import sys

input = sys.stdin.readline
t = int(input())


def solution1(n, m, data):
    matrix = [data[(m * i): (m * (i + 1))] for i in range(n)]

    dp = [(0, 0)] * m
    dp[0] = max([(matrix[x][0], x) for x in range(n)])

    for i in range(m - 1):
        max_value, x = dp[i]
        next_max_value = 0
        for dx in [-1, 0, 1]:
            nx = x
            if x + dx < 0 or x + dx >= n:
                continue

            if matrix[x + dx][i + 1] > next_max_value:
                next_max_value = matrix[x + dx][i + 1]
                nx = x + dx

        dp[i + 1] = max_value + next_max_value, nx

    print(dp[m - 1][0])


def solution2(n, m, data):
    dp = [data[(m * i): (m * (i + 1))] for i in range(n)]  # 데이터로 dp 테이블 초기화
    for y in range(1, m):
        for x in range(n):
            # 현재 위치 기준 왼쪽 위에서 오는 경우 = 왼쪽 위의 값 + 현재 위치 값
            left_up = dp[x - 1][y - 1] if x - 1 >= 0 else 0
            # 현재 위치 기준 왼쪽에서 오는 경우
            left = dp[x][y - 1]
            # 현재 위치 기준 왼쪽 아래에서 오는 경우
            left_down = dp[x + 1][y - 1] if x + 1 < n else 0

            dp[x][y] = max(left_up, left, left_down) + dp[x][y]

    print(max([dp[i][m - 1] for i in range(n)]))


for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    # solution1(n, m, data)
    solution2(n, m, data)
