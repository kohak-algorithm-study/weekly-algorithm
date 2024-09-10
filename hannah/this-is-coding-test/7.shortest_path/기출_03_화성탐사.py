'''
당신은 화성 탐사 기계를 개발하는 프로그래머입니다.
그런데 화성은 에너지 공급원을 찾기가 힘듭니다.
그래서 에너지를 효율적으로 사용하고자 화성 탐사 기계가 출발 지점에서 목표 지점까지 이동 할 때 항상 최적의 경로를 찾도록 개발해야 합니다.
화성 탐사 기계가 존재하는 공간은 N X N 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용(에너지 소모량)이 존재합니다.
가장 왼쪽 위 칸인 [0][0] 위치에서 가장 오른쪽 아래 칸인 [N - 1][N - 1] 위치로 이동하는 최소 비용을 출력하는 프로그램을 작성하세요.
화성 탐사 기계는 특정한 위치에서 상하좌우 인접한 곳으로 1칸씩 이동할 수 있습니다.

- 입력 조건
• 첫째 줄에 테스트 케이스의 수 T(1 <= T <= 10)가 주어집니다.
• 매 테스트 케이스의 첫째 줄에는 탐사 공간의 크기를 의미하는 정수 N이 주어집니다. (2 <= N <= 125)
  이어서 N개의 줄에 걸쳐 각 칸의 비용이 주어지며 공백으로 구분합니다. (0 <= 각 칸의 비용 <= 9)

- 출력 조건
• 각 테스트 케이스마다 [0][0]의 위치에서 [N - 1][N - 1]의 위치로 이동하는 최소 비용을 한 줄에 하나씩 출력합니다.

- 입력 예시
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4

- 출력 예시
20
19
36
'''
import heapq
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    n = int(input())
    gragh = [list(map(int, input().split())) for _ in range(n)]

    INF = 9 * 125
    cost_table = [[INF] * n for _ in range(n)]
    cost_table[0][0] = gragh[0][0]
    heap = []
    heapq.heappush(heap, (gragh[0][0], 0, 0))

    while heap:
        cost, x, y = heapq.heappop(heap)

        # if x == (n - 1) and y == (n - 1):
        #     break

        if cost_table[x][y] < cost:  # 이미 처리된 곳은 패스
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if cost_table[x][y] + gragh[nx][ny] < cost_table[nx][ny]:  # dlal
                cost_table[nx][ny] = cost_table[x][y] + gragh[nx][ny]  # 더 작은 값으로 갱신
                heapq.heappush(heap, (cost_table[nx][ny], nx, ny))

    print(cost_table[n - 1][n - 1])