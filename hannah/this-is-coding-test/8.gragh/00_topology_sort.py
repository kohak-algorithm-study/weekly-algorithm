'''
[위상 정렬]
위상 정렬(Topology Sort)은 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것을 의미한다.
즉, 순서가 정해져 있는 일녕의 작업을 차례대로 수행해야 할 때 사용할 수 있는 알고리즘이다.
ex) 선수과목을 고려한 학습 순서 설정

DFS로 구현할 수도 있고, 큐를 이용해서 구현할 수도 있다.
- 진입 차수(indegree): 특정 노드로 들어오는 간선의 개수
- 진출 차수: 특정 노드에서 나가는 간선의 개수
큐를 이용해서 구현하는 방법
1. 진입 차수가 0인 모든 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음 과정을 반복한다.
  1) 큐에서 원소를 꺼내서 해당 노드에서 나가는 간선을 그래프에서 제거한다.
  2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
결과적으로 각 노드가 큐에 들어온 순서가 위상 정렬을 수행한 결과와 같다.
** 사이클이 있는 그래프의 경우, 모든 노드의 진입 차수가 1이상이다. 따라서 이 알고리즘을 적용할 수 없다.
'''
from collections import deque

v, e = map(int, input().split())  # v=노드 개수, e=간선 개수
gragh = [[] for _ in range(v + 1)]  # 방향 그래프
indegree = [0] * (v + 1)  # 각 노드 별 진입 차수

for _ in range(e):
    a, b = map(int, input().split())
    gragh[a].append(b)
    indegree[b] += 1  # b의 진입차수 1 증가


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        current_node = q.popleft()
        result.append(current_node)

        for i in range(gragh[current_node]):
            indegree[i] -= 1  # 연결된 다음 노드의 진입차수에서 1 차감

            if indegree[i] == 0:
                q.append(i)

    print(*result)


topology_sort()
