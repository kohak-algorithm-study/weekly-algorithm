'''
https://www.acmicpc.net/problem/14502
'''
# 시간초과!!!

import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())  # n: 세로, m: 가로
gragh = []

for _ in range(n):
    gragh.append(list(map(int, input().rstrip().split())))


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_safe_cnt = 0


# 벽 3개 세우기 + 바이러스 감염 시나리오
def make_wall(wall_cnt):

    if wall_cnt == 3:
        # 벽을 다 세우면 바이러스 퍼트리기
        infect_with_virus()
        return

    # 현재 빈칸(==0)인 곳에 벽 세우기
    for i in range(n):
        for j in range(m):
            if gragh[i][j] == 0:
                gragh[i][j] = 1
                make_wall(wall_cnt + 1)
                gragh[i][j] = 0  # 원복(백트래킹)


# bfs를 이용해서 바이러스 감염시키기
def infect_with_virus():
    temp_gragh = deepcopy(gragh)
    q = deque()  # 바이러스 위치 저장

    for i in range(n):
        for j in range(m):
            if temp_gragh[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if temp_gragh[nx][ny] == 0:
                temp_gragh[nx][ny] = 2
                q.append((nx, ny))

    global max_safe_cnt
    temp_safe_cnt = get_safe_cnt(temp_gragh)
    if temp_safe_cnt > max_safe_cnt:
        max_safe_cnt = temp_safe_cnt

    return


# 안전영역 개수 구하기
def get_safe_cnt(g):
    cnt = 0
    for i in range(n):
        cnt += g[i].count(0)  # 리스트 중에서 값이 0인 것의 개수
    return cnt


make_wall(0)
print(max_safe_cnt)
