'''
https://www.acmicpc.net/problem/16234
'''
import sys
from collections import deque

input = sys.stdin.readline

n, min_limit, max_limit = map(int, input().rstrip().split())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])
    unions = [(start_x, start_y)]  # 이번에 합쳐지는 국가의 위치를 저장

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n or visited[nx][ny] == 1:
                continue

            if min_limit <= abs(a[x][y] - a[nx][ny]) <= max_limit:
                visited[nx][ny] = 1
                q.append((nx, ny))
                unions.append((nx, ny))

    return unions


def update_a(unions):
    new_value = sum(a[x][y] for x, y in unions) // len(unions)
    for x, y in unions:
        a[x][y] = new_value
    return


day = 0
while True:
    visited = [[0] * n for _ in range(n)]
    flag = 0
    # 각 위치에서 bfs(완전 탐색) - 단, 이전에 방문했던 곳은 제외
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                unions = bfs(i, j)

                if len(unions) > 1:
                    flag = 1
                    update_a(unions)

    if flag == 0:
        break

    # while문이 종료되지 않았다면 완전탐색을 한번 수행한 것이므로 day += 1
    day += 1

print(day)
