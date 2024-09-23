'''
서로소 집합 자료구조(union-find 자료구조)

서로서 집합 알고리즘을 사용하는 예시
- 같은 그룹인지 확인할 때: union 연산을 통해 주어진 노드들의 루트 노드가 같으면 같은 그룹임을 알 수 있다.
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

# 부모 노드 테이블 초기화
parent = [0] * (v + 1)
for i in range(1, v + 1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    x, y = map(int, input().split())
    union_parent(parent, x, y)

print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")
