def solution(n: int, calculations: list) -> list:
    answer = []
    parent = []

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

    for i in range(n+1):
        parent.append(i)

    for calc in calculations:
        if calc[0] == 0:
            union_node(calc[1], calc[2], parent)
        else:
            if find_parent(calc[1], parent) == find_parent(calc[2], parent):
                answer.append("YES")
            else:
                answer.append("NO")

    return answer


n = 7
calculations = [
    [0, 1, 3],
    [1, 1, 7],
    [0, 7, 6],
    [1, 7, 1],
    [0, 3, 7],
    [0, 4, 2],
    [0, 1, 1],
    [1, 1, 1]
]

print(solution(n, calculations))  # [NO, NO, YES]
