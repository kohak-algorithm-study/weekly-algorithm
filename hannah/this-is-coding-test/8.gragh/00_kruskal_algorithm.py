'''
[신장 트리(Spanning Tree)]
하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건을 만족해야 한다.

[크루스칼 알고리즘]
최소 비용의 신장 트리
ex) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치해야 할 때, 모든 도시를 최소한의 비용으로 모든 도시를 연결하려면?
'''


def find_parent(parent, x):  # 루트 노드를 찾는 함수지만, 통상적으로 함수 이름을 find_parent로 짓는다
    if parent[x] != x:  # 부모 노드가 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y


v, e = map(int, input().split())  # v=노드 개수, e=간선 개수
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
min_cost = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

# 비용기준으로 오름차순 정렬
edges.sort()

for cost, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost

print(min_cost)
