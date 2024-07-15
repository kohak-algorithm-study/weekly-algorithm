'''
https://www.acmicpc.net/problem/14554
'''

import heapq
import sys

input = sys.stdin.readline
N, M, S, E = map(int, input().split())

gragh = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, dist = map(int, input().split())
    gragh[a].append((b, dist))
    gragh[b].append((a, dist))

INF = int(1e9)
min_dist = [INF] * (N + 1)
min_dist[S] = 0


q = []
heapq.heappush(q, (0, S))

for node, dist in gragh[S]:
    heapq.heappush(q, (dist, node))

min_path_counts = [0] * (N + 1)
min_path_counts[S] = 1

while q:
    print()
    print("===========whlie 시작============")
    print(q)
    target_node_dist, target_node = heapq.heappop(q)

    print(f'====target_node: {target_node}====')
    print(f'S부터 target_node까지 거리: {min_dist[target_node]}')
    print(f'target_node까지 최단 경로 개수: {min_path_counts[target_node]}')

    if min_dist[target_node] < target_node_dist:
        print("이미 처리된 노드이므로 pass")
        continue

    print(f'target_node와 연결된 노드, 거리 출력: {gragh[target_node]}')
    for linked_node, linked_node_dist in gragh[target_node]:
        print("-----")
        print(f'linked_node: {linked_node}')
        print(f'S노드에서 {target_node}번 노드를 거쳐서 {linked_node}번 노드로 이동한다면')
        cost = min_dist[target_node] + linked_node_dist
        print(f'cost = {cost}')
        print(f'현재 linked_node까지의 최단 경로: {min_dist[linked_node]}')
        print(f'현재 최단경로로 target_node까지 가는 방법의 수: {min_path_counts[target_node]}')
        print(f'현재 최단경로로 linked_node까지 가는 방법의 수: {min_path_counts[linked_node]}')

        if cost < min_dist[linked_node]:
            print("---최단 경로 갱신---")
            print(f"S부터 linked_node까지의 거리: {cost}")
            min_dist[linked_node] = cost
            heapq.heappush(q, (cost, linked_node))
            min_path_counts[linked_node] = min_path_counts[target_node]  # 최초로 최단경로를 구했을 때, 최단경로의 갯수는 target_node를 거쳤을 때의 최단경로의 갯수와 같다
            print(f'{linked_node}까지의 최단 경로 개수 갱신: {min_path_counts[linked_node]}')
            # 최단 경로가 갱신된다고 해도, min_path_counts[target_node]로 초기화 한다.

        elif cost == min_dist[linked_node]:
            print("---동일한 최단 경로---")
            min_path_counts[linked_node] += min_path_counts[target_node]
            print(f'{linked_node}까지의 최단 경로 개수 갱신: {min_path_counts[linked_node]}')

print()
print("=============================")
print(*min_path_counts)
print(min_path_counts[E] % (int(1e9) + 9))
