# BFS 기초 코드
from collections import deque


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()  # q에서 첫번째 원소 꺼내기
        print(v, end=" ")
        
        for i in gragh[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


gragh = [
    [],  # 노드가 1부터 시작하므로 0번 노드에 대한 것은 비워둔다
    [2, 3, 8],  # 1번 노드(1은 gragh list의 인덱스)가 2, 3, 8번 노드와 연결되어 있음을 의미.
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

bfs(gragh, 1, visited)  # 시작노드가 1번



