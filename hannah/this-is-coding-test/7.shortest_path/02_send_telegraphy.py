'''
[전보]
어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
예를 들어 X에서 Y로 향하는 통로는 있지만, Y에서 X로 향화는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다.
또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.

어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때,
도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.


- 입력 조건
• 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다. (1 <= N <= 30_000, 1 <= M <= 200_000, 1 <= C <= N)
• 둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
  이는 특정 도시 X에서 다른 특정 도시 Y로 이어자는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다.
  (1 <= X, Y <= N, 1 <= Z <= 1000)

- 출력 조건
• 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.


- 입력 예시
3 2 1
1 2 4
1 3 2

- 출력 예시
2 4
'''

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
min_dist = [INF] * (N + 1)  # 최단 거리 테이블(C에서 index번호 노드 까지의 최단 거리를 말함)

gragh = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y, z = map(int, input().split())
    gragh[x].append((y, z))

q = []
heapq.heappush(q, (0, C))
min_dist[C] = 0   # 자기 자신노드는 0으로 초기화

for city, dist in gragh[C]:
    heapq.heappush(q, (dist, city))

while q:
    dist, target_city = heapq.heappop(q)

    # 이미 처리한 노드는 pass
    if dist < min_dist[target_city]:
        continue

    for linked_city, linked_city_d in gragh[target_city]:
        cost_for_pass_linked_city = min_dist[target_city] + linked_city_d

        # 현재 노드(target_city)를 거쳐서 인접 노드로 가는 경우가 더 짧은 경우
        if cost_for_pass_linked_city < min_dist[linked_city]:  # target_city를 거쳐서 온 거리가 linked_city까지의 최단거리보다 작으면
            min_dist[linked_city] = cost_for_pass_linked_city
            heapq.heappush(q, (linked_city_d, linked_city))


cnt = 0
max_value = 0
for d in min_dist:
    if d != INF and d != 0:
        cnt += 1
        if d > max_value:
            max_value = d

print(f'{cnt} {max_value}')
