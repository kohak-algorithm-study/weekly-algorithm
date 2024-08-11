import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

test_tube = []
data = []

for i in range(n):
    test_tube.append(list(map(int, input().split())))

    for j in range(n):
        data.append((test_tube[i][j], 0, i, j ))

s, x, y = map(int, sys.stdin.readline().rstrip().split())


data.sort()
q = deque(data)

dx = [-1,0,1,0]
dy = [0,1,0,-1]


while(q):
    virus, s, x, y = q.popleft()

    if s == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= any and ny < n:
            if test_tube[nx][ny] == 0:
                test_tube[nx][ny] = virus
                q.append(virus, s+1, nx, ny)

print(test_tube[x-1][y-1])