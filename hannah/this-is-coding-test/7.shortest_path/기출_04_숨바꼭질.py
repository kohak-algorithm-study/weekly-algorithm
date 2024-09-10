'''
동빈이는 숨바꼭질을 하면서 술래로부터 잡히지 않도록 숨을 곳을 찾고 있습니다.
동빈이는 1 〜 N번까지의 헛간 중에서 하나를 골라 숨을 수 있으며,
술래는 항상 1번 헛간에서 출발합니다.
전체 맵에는 총 M개의 양방향 통로가 존재하며, 하나의 통로는 서로 다른 두 헛간을 연결합니다.
또한 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어집니다.
동빈이는 1번 헛간으로부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단하고 있습니다.
이때 최단 거리의 의미는 지나야 하는 길의 최소 개수를 의미합니다.
동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성하세요.

- 입력 조건
• 첫째 줄에는 N과 M이 주어지며, 공백으로 구분합니다. (2 <= N <= 20,000), (1 <= M <= 50,000)
• 이후 M개의 줄에 걸쳐서 서로 연결된 두 헛간 A와 B의 번호가 공백으로 구분되어 주어집니다.  (1 <= A, B <= N)

- 출력 조건
• 첫 번째는 숨어야 하는 헛간 번호를 (만약 거리가 같은 헛간이 여러 개면 가장 작은 헛간 번호를 출력합니다),
  두 번째는 그 헛간까지의 거리를, 세 번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력해야합니다.

- 입력 예시
6 7
3 6
4 3
3 2
1 3
1 2
2 4
5 2

- 출력 예시
4 2 3
'''
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
gragh = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    gragh[a].append(b)
    gragh[b].append(a)

INF = int(1e9)
distance = [INF] * (n + 1)  # 1번부터 각 노드까지의 최단거리
distance[0] = -1  # 사용하지 않는 인덱스라 음수로 초기화
distance[1] = 0  # 1번 자기 자신까지의 거리는 0으로 초기화
visited = [False] * (n + 1)

heap = []
heapq.heappush(heap, (0, 1))

while heap:
    d, node = heapq.heappop(heap)

    if (distance[node] < d) or (visited[node] and distance[node] >= d):  # 이미 최소 값을 구한 경우
        continue

    visited[node] = True
    for linked_node in gragh[node]:
        new_d = min(distance[node] + 1, distance[linked_node])
        distance[linked_node] = new_d
        heapq.heappush(heap, (new_d, linked_node))


max_d = max(distance)
found = distance.index(max_d)
cnt = distance.count(max_d)
print(found, max_d, cnt)
