'''
[음료수 얼려먹기]
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0. 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.

다음의 4x5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.
00110
00011
11111
00000

- 입력 예시
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

- 출력 예시
8

'''
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().rstrip())))

result = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if matrix[x][y] == 0:  # 연결된 노드이면서 방문하지 않은 노드
        matrix[x][y] = 1  # 방문처리

        # 인접한 노드를 dfs로 탐색한다(재귀 호출)
        for i in range(4):  # 상, 하, 좌, 우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    # 방문할 노드가 없으면 탐색 끝
    return False


for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
