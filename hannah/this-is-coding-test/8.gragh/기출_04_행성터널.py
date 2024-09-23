'''
https://www.acmicpc.net/problem/2887
'''
import sys

input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n = int(input())
parent = [i for i in range(n)]

# 메모리 초과!!!
# planets = []
# for number in range(n):
#     x, y, z = map(int, input().split())
#     planets.append((x, y, z, number))

# tunnels = []
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         x1, y1, z1 = planets[i]
#         x2, y2, z2 = planets[j]
#         cost = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
#         tunnels.append((cost, i, j))
# tunnels.sort()

x_data = []  # 각 행성의 x좌표와 행성 번호를 저장
y_data = []  # 각 행성의 y좌표와 행성 번호를 저장
z_data = []  # 각 행성의 z좌표와 행성 번호를 저장
for i in range(n):
    x, y, z = map(int, input().split())
    x_data.append((x, i))
    y_data.append((y, i))
    z_data.append((z, i))

x_data.sort()
y_data.sort()
z_data.sort()

tunnels = []
for i in range(1, n):
    # 각 축에 대해 (지금 행성에서 이전 행성 까지의 비용, 이전 행성 번호, 지금 행성 번호)을 저장
    tunnels.append((x_data[i][0] - x_data[i - 1][0], x_data[i - 1][1], x_data[i][1]))
    tunnels.append((y_data[i][0] - y_data[i - 1][0], y_data[i - 1][1], y_data[i][1]))
    tunnels.append((z_data[i][0] - z_data[i - 1][0], z_data[i - 1][1], z_data[i][1]))
tunnels.sort()

result_cost = 0
for cost, x, y in tunnels:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result_cost += cost

print(result_cost)
