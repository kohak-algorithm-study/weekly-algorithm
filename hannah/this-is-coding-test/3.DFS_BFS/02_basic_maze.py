'''
[미로 탈출]
동빈이는 N X M 크기의 직사각형 형태의 미로에 갇혀 있다.
미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
미로는 반드시 탈출할 수 있는 형태로 제시된다.

이때 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
단, 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

- 입력 예시
5 6
101010
111111
000001
111111
111111

- 출력 예시
10
'''
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# for _ in range(n):
#     matrix.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


q = deque([(0, 0)])
while q:
    x, y = q.popleft()

    # 인접한 노드 모두 큐에 담기
    for i in range(4):  # 상, 하, 좌, 우 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
            continue

        if matrix[nx][ny] == 0:
            continue

        # 해당 노드를 처음 방문하는 경우(==1)에만 cnt 증가
        if matrix[nx][ny] == 1:  # 이미 방문한 경우에는 1이 아니므로 패스된다
            matrix[nx][ny] = matrix[x][y] + 1
            q.append((nx, ny))

print(matrix[n - 1][m - 1])
