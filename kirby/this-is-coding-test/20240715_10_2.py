def solution(n: int, paths: list) -> int:

    def find_parent(a: int, parent: list) -> int:
        if a != parent[a]:
            parent[a] = find_parent(parent[a], parent)
        return parent[a]

    def union_node(a: int, b: int, parent: list):
        a_parent = find_parent(a, parent)
        b_parent = find_parent(b, parent)
        if a_parent > b_parent:
            parent[a_parent] = b_parent
        else:
            parent[b_parent] = a_parent

    parent = []
    for i in range(n+1):
        parent.append(i)

    edges = []
    answer_edges = []
    for path in paths:
        edges.append([path[2], path[0], path[1]])

    edges.sort()
    for edge in edges:
        cost = edge[0]
        a = edge[1]
        b = edge[2]
        if find_parent(a, parent) != find_parent(b, parent):
            answer_edges.append(cost)
            union_node(a, b, parent)

    return sum(answer_edges[:-1])


n = 7
paths = [
    [1, 2, 3],
    [1, 3, 2],
    [3, 2, 1],
    [2, 5, 2],
    [3, 4, 4],
    [7, 3, 6],
    [5, 1, 5],
    [1, 6, 2],
    [6, 4, 1],
    [6, 5, 3],
    [4, 5, 3],
    [6, 7, 4],
]
print(solution(n, paths))  # 8
