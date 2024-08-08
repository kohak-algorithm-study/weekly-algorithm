'''
https://www.acmicpc.net/problem/18352
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M, K, start = map(int, input().rstrip().split())
gragh = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    gragh[a].append(b)

visited = [False] * (N + 1)
dist = [-1] * (N + 1)

# 1번 노드에서 출발
q = deque([start])
visited[start] = True
dist[start] = 0


# bfs
while q:
    now = q.popleft()
    # print(f'{now}까지의 최단거리: {dist[now]}')

    for adj_node in gragh[now]:
        # print("--------------")
        # print(f'adj: {adj_node}')
        # print(f'visited: {visited[adj_node]}')
        if not visited[adj_node]:
            q.append(adj_node)
            visited[adj_node] = True
            dist[adj_node] = dist[now] + 1  # now까지의 최단경로를 거치고 adj_node에 접근하므로


is_exiting = False
for i in range(1, N + 1):
    if dist[i] == K and i != start:
        print(i)
        is_exiting = True

if not is_exiting:
    print(-1)
