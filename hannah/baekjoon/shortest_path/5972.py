'''
https://www.acmicpc.net/problem/5972
'''
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
gragh = [[] for _ in range(1 + N)]
for _ in range(M):
    a, b, dist = map(int, input().split())
    gragh[a].append((b, dist))
    gragh[b].append((a, dist))

start = 1
min_dist = [INF] * (N + 1)
min_dist[start] = 0

q = []
heapq.heappush(q, (0, start))
for node, dist in gragh[start]:
    heapq.heappush(q, (dist, node))

while q:
    dist, target_node = heapq.heappop(q)

    if min_dist[target_node] < dist:
        continue

    for linked_node, linked_node_dist in gragh[target_node]:
        cost = linked_node_dist + min_dist[target_node]  # start에서 target까지의 거리 + target에서 linked_node까지의 거리
        if cost < min_dist[linked_node]:  # vs start에서 linked_node까지의 거리
            min_dist[linked_node] = cost
            heapq.heappush(q, (cost, linked_node))

print(min_dist[N])
