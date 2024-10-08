'''
한 마을은 N개의 집과 M개의 도로로 구성되어 있습니다. 각 집은 0번부터 N - 1번까지의 번호로 구분됩니다.
모든 도로에는 가로등이 구비되어 있는데, 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일합니다.
예를 들어 2번 집과 3번 집 사이를 연결하는 길이가 7인 도로가 있다고 해봅시다.
하루 동안 이 가로등을 켜기 위한 비용은 7이 됩니다.
정부에서는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 합니다.
결과적으로 일부 가로등을 비활성화하여 최대한 많은 금액을 절약하고자 합니다.
마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하세요.

[입력 조건]
• 첫째줄에 집의 수 N(1 <= N <= 200,000)과 도로의 수 M(N-1 <= M <= 200,000)이 주어집니다.
• 다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X, Y, Z가 주어지며, 공백으로 구분합니다. (0 <= X, Y < N)
  이는 X번 집과 Y번 집 사이에 양방향 도로가 있으며, 그 길이가 Z라는 의미입니다. 단 X와 Y가 동일한 경우는 없으며 마을을 구성하는 모든 도로의 길이 합은 2^31보다 작습니다.

[출력 조건]
• 첫째 줄에 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력합니다.

[입력 예시]
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11

[출력 예시]
51
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n)]

edges = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))

edges.sort()


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


used_cost = 0

# 모든 간선에 대해서 최소 신장 트리에 포함시킬지 탐색
for cost, x, y in edges:
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        used_cost += cost

total_cost = sum(edge[0] for edge in edges)
print(total_cost - used_cost)
