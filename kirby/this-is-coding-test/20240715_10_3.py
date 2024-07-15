from collections import deque


def solution(n: int, classes: list) -> list:
    answer = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    incounts = [0] * (n+1)

    for i in range(1, len(classes)):
        answer[i] = classes[i][0]
        for pre_class in classes[i][1:-1]:
            graph[pre_class].append(i)
            incounts[i] += 1

    queue = deque([])
    for i in range(1, len(incounts)):
        if incounts[i] == 0:
            queue.append(i)

    while queue:
        now_class = queue.popleft()
        for next_class in graph[now_class]:
            answer[next_class] = max(answer[next_class], answer[now_class] + classes[next_class][0])
            incounts[next_class] -= 1
            if incounts[next_class] == 0:
                queue.append(next_class)

    return answer[1:]


n = 5
classes = [
    [-1],
    [10, -1],
    [10, 1, -1],
    [4, 1, -1],
    [4, 3, 1, -1],
    [3, 3, -1]
]
print(solution(n, classes))  # [10, 20, 14, 18, 17]
