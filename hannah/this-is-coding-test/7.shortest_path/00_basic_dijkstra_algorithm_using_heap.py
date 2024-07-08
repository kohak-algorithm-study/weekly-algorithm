'''
[다익스트라 최단 경로 알고리즘]
한 지점에서 다른 모든 지점까지의 최단 거리 구하기

[기본 예제]
- 입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''
# 가장 짧은 거리를 갖는 노드를 찾을 때 우선순위 큐를 이용하는 방식으로 구현


import heapq
import sys

INF = int(1e9)  # 무한을 의미하는 값으로 10억이라고 설정

n, m = map(int, sys.stdin.readline().rstrip().split())  # n: 노드 개수, m: 간선 개수
start = int(sys.stdin.readline().rstrip())  # 시작 노드 번호
gragh = [[] for _ in range(n + 1)]  # 노드들 간의 연결 정보를 담는 테이블(방향 그래프)
# 예) gragh[1] = [(2, 10) (4, 3)]: 1번 노드에는 2번 노드와 4번 노드가 연결되어 있고, 각각의 거리는 10, 3이다.

distance = [INF] * (n + 1)  # 최단 거리 테이블(INF로 초기화)

for _ in range(m):
    a, b, x = map(int, sys.stdin.readline().rstrip().split())  # a노드에서 b노드까지의 거리가 x다.
    gragh[a].append((b, x))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (x, y) == y번 노드까지의 거리가 x라는 의미. x를 먼저 쓴 이유는 x를 기준으로 오름차순으로 정렬하기 위함이다.
    # 시작 노드에 대해서 초기화
    distance[start] = 0  # 자기 자신과의 거리는 0

    for linked_node, d in gragh[start]:
        distance[linked_node] = d
        heapq.heappush(q, (d, linked_node))

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복
    while q:
        # heap에 push할 때 우선순위대로 값이 정렬되므로 pop을 하면 x가 가장 작은, 즉, 거리가 가장 짧은 노드부터 나온다
        d, target_node = heapq.heappop(q)

        if d < distance[target_node]:  # target_node까지의 거리가 d 보다 작다는 것은 이미 최소값을 갱신되었다는 의미. 즉, 이 노드는 이미 방문처리 되었다는 것을 의미한다.
            continue

        for linked_node, d in gragh[target_node]:
            if distance[target_node] + d < distance[linked_node]:  # 현재 처리중인 노드(target_node)를 거처서 갈때가 더 빠른지 확인
                distance[linked_node] = distance[target_node] + d
                heapq.heappush(q, (distance[target_node] + d, linked_node))


dijkstra(start)

# start 노드에서 모든 노드로 갈 때 각각의 최단 거리 출력
for i in range(1, n + 1):
    if i == start:
        continue

    if distance[i] == INF:
        print(f"{i}번 노드까지의 최단거리: 갈 수 없음")
    else:
        print(f"{i}번 노드까지의 최단거리: {distance[i]}")
