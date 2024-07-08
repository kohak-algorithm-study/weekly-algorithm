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

'''
[입력 예시]
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

[출력 예시]
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0

'''