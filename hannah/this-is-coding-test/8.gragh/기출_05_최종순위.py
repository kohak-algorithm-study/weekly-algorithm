'''
https://www.acmicpc.net/problem/3665
'''
import sys
from collections import deque

input = sys.stdin.readline


for _ in range(int(input())):
    result = []
    n = int(input())
    last_year = list(map(int, input().split()))

    # 진입 차수 초기화
    indegree = [0] * (n + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬(n+1)*(n+1) 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):  # 대칭이므로 range(n)을 다 할 필요가 없음
            graph[last_year[i]][last_year[j]] = True
            indegree[last_year[j]] += 1

    m = int(input())  # 작년과 비교했을 때, 등수가 바뀐 쌍의 수
    for _ in range(m):
        a, b = map(int, input().split())  # a -> b로 변경된 것
        if graph[a][b]:  # 바로 앞에 붙어있는 경우라면
            graph[a][b] = False
            graph[b][a] = True  # 연결 관계 재정립
            indegree[a] += 1
            indegree[b] -= 1
        else:  # 바로 옆에 붙어 있지 않은 경우
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상 정렬
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True  # 위상 정렬 결과가 오직 하나인지의 여부
    cycle = False  # 그래프 내에 사이클이 존재하는지에 대한 여부

    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미(진입 차수가 0인 노드가 없다는 뜻이므로)
        if len(q) == 0:
            cycle = True
            break

        # 큐에 원소가 2개 이상이면 가능한 위상 정렬이 여러 개 라는 의미 -> 문제의 답을 구할 수 없음
        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(*result)
