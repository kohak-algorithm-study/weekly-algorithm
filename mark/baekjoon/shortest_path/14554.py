import heapq
import sys

INF = int(1e9)  # 무한을 의미하는 값으로 10억이라고 설정

n, m, s, e = map(int, sys.stdin.readline().rstrip().split())

start = s # 시작 노드 번호
gragh = [[] for _ in range(n + 1)]  # 노드들 간의 연결 정보를 담는 테이블(방향 그래프)

distance = [INF] * (n + 1)  # 최단 거리 테이블(INF로 초기화)
count = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())  # a노드에서 b노드까지의 거리가 x다.
    gragh[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    for linked_node, d in gragh[start]:
        distance[linked_node] = d
        heapq.heappush(q, (d, linked_node))

    while q:
        d, target_node = heapq.heappop(q)

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


'''
3 4 1 3
1 2 1
2 1 1
2 3 1
1 3 2
'''
