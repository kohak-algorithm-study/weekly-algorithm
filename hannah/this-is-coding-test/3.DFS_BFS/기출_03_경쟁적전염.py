'''
https://www.acmicpc.net/problem/18405
'''

import sys
from collections import deque


def bfs(q):
    global s
    spend_s = 0
    while q:
        virus_num, x, y = q.popleft()
        if q:
            next_virus_num = q[0][0]
        else:
            next_virus_num = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if gragh[nx][ny] == 0:
                gragh[nx][ny] = virus_num
                q.append((gragh[nx][ny], nx, ny))

        if next_virus_num < virus_num:
            spend_s += 1

        if spend_s == s:
            break


def get_virus_q():
    q = deque()
    for i in range(n):
        for j in range(n):
            if gragh[i][j] != 0:
                q.append((gragh[i][j], i, j))
    return deque(sorted(q))


if __name__ == "__main__":
    input = sys.stdin.readline
    n, k = map(int, input().rstrip().split())
    gragh = []
    for _ in range(n):
        gragh.append(list(map(int, input().rstrip().split())))
    s, x, y = map(int, input().rstrip().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    if s > 0:
        virus_q = get_virus_q()
        bfs(virus_q)

    print(gragh[x - 1][y - 1])
