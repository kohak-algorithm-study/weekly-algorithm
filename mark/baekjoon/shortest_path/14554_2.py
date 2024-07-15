import heapq
import sys

input = sys.stdin.read
INF = int(1e9)  # 무한을 의미하는 값으로 10억이라고 설정
MOD = 1000000009


def dijkstra(n, start, graph):
    distance = [INF] * (n + 1)  # 최단 거리 테이블(INF로 초기화)
    count = [0] * (n + 1)  # 최단 경로의 수를 저장할 리스트
    distance[start] = 0
    count[start] = 1

    q = []
    heapq.heappush(q, (0, start))

    while q:
        d, target_node = heapq.heappop(q)

        if d > distance[target_node]:
            continue

        for linked_node, weight in graph[target_node]:
            new_dist = d + weight
            if new_dist < distance[linked_node]:  # 더 짧은 경로 발견
                distance[linked_node] = new_dist
                count[linked_node] = count[target_node]
                heapq.heappush(q, (new_dist, linked_node))
            elif new_dist == distance[linked_node]:  # 같은 길이의 경로 발견
                count[linked_node] = (count[linked_node] + count[target_node]) % MOD

    return distance, count


def main():
    input_data = input().strip().split()
    n, m, s, e = map(int, input_data[:4])
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a = int(input_data[4 + 3 * i])
        b = int(input_data[4 + 3 * i + 1])
        c = int(input_data[4 + 3 * i + 2])
        graph[a].append((b, c))
        graph[b].append((a, c))  # 양방향 그래프 설정

    distance, count = dijkstra(n, s, graph)

    print(count[e])


if __name__ == "__main__":
    main()
