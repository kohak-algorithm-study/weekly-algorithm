'''
https://www.acmicpc.net/problem/11404
'''
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

distance = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())

    if distance[start][end] == INF:
        distance[start][end] = cost
    else:
        distance[start][end] = min(cost, distance[start][end])


# k가 for문 가장 바깥으로와야 함.
# k가 for문 가장 안쪽으로 간다면, 1에서 출발해서 2로 가는 경로를 구할 때 1 -> k -> 2 경로만 구할 수 있다.
# 하지만 1에서 출발해서 2로 가는 경로를 구하려면, 1 -> k -> 2 만 구하면 되는게 아니라, 1 -> k1 -> k2 -> k3.. -> 2로 가는 경로를 모두 계산해야 하기 때문
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                distance[i][j] = 0
                continue

            if i != k and j != k:
                distance[i][j] = min(distance[i][k] + distance[k][j], distance[i][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distance[i][j] == INF:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()
