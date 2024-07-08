'''
[플로이드-워셜 알고리즘]
모든 노드에서 다른 모든 노드까지의 최단 거리 구하기
다익스트라 알고리즘과 다른 점은 매 단계마다 방문하지 않은 노드 중 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않다.
플로이드-워셜 알고리즘은 다이나믹 프로그래밍 유형에 속한다.
점회식에 맞게 2차원 테이블에 최단 거리 정보를 저장한다.
플로이드-워셜 알고리즘은 O(n^3)이기 때문에 노드의 개수가 500개 이하로 주어진다. 그럼에도 시간 초과 판정을 받을 수도 있다. 이럴때는 다른 알고리즘

[기본 예제]

- 입력 예시
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

'''

import sys

# input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억이라고 설정

n = int(sys.stdin.readline().rstrip())  # 노드 개수
m = int(sys.stdin.readline().rstrip())  # 간선 개수

dp = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, x = map(int, sys.stdin.readline().rstrip().split())  # a노드에서 b노드까지의 거리가 x다.
    dp[a][b] = x

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            dp[a][b] = 0


for k in range(1, n + 1):  # k는 거처가는 노드를 의미
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])


# start 노드에서 모든 노드로 갈 때 각각의 최단 거리 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            continue

        if dp[i][j] == INF:
            print(f"{i}번에서 {j}번 노드까지의 최단거리: 갈 수 없음")
        else:
            print(f"{i}번에서 {j}번 노드까지의 최단거리: {dp[i][j]}")
