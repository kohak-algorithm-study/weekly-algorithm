# DFS 기초 코드(재귀함수 사용)

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    
    for i in graph[v]:  # 노드 v와 인접한 노드를 탐색
        if not visited[i]:
            dfs(graph, i, visited)


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

dfs(gragh, 1, visited)  # 시작노드가 1번



