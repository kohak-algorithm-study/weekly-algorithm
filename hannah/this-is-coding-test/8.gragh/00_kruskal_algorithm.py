'''
[신장 트리(Spanning Tree)]
하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프를 의미
이때 모든 노드가 포함되어 서로 연결되면서 사이클이 존재하지 않는다는 조건을 만족해야 한다.
쉽게 말해, 그래프가 모든 노드를 다 포함하지만 모든 노드가 서로 연결되어 있는 것은 아니고, 최소한의 간선만 이용한 그래프. 사이클이 발생하면 신장트리가 아니다.
그래서 "최소 신장 트리"에 활용된다. 즉, 최소 비용으로 트리를 만들어야 한다 == 신장 트리를 만들어야 한다.

** 참고로, 최소 신장 트리의 간선의 개수 = (노드 개수 - 1) 이다.

** 신장 트리에 union 연산을 하는 이유
: 주어진 그래프에서 모든 노드에 대해 union 연산을 했을 때, 루트 노드가 같은 것이 있다면 사이클이 있다는 의미

[크루스칼 알고리즘]
대표적인 최소 비용의 신장 트리 알고리즘. 그리디 알고리즘으로 분류됨
ex) N개의 도시가 존재하는 상황에서 두 도시 사이에 도로를 놓아 전체 도시가 서로 연결될 수 있게 도로를 설치해야 할 때, 모든 도시를 최소한의 비용으로 모든 도시를 연결하려면?

크루스칼 알고리즘 과정
1. 간선 데이터를 비용에 따라 오름차순으로 정렬
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
   2-1. 사이클이 발생하지 않는다면(=같은 집합에 속해있지 않으면=루트 노드가 같지 않으면) 최소 신장 트리에 포함시킨다. -> union 연산 수행
   2-2. 사이클이 발생한다면 최소 신장 트리에 포함시키지 않는다. -> 무시하고 넘어가기
3. 모든 간선에 대해 2번 과정을 반복
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
    if find_parent(parent, a) != find_parent(parent, b):  # 루트 노드가 같지 않으면 같은 그룹이 아니므로 union연산을 해서 신장트리에 포함시킨다
        union_parent(parent, a, b)
        min_cost += cost

print(min_cost)
