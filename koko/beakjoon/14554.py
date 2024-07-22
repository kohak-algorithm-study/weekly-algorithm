import heapq
import sys
from collections import defaultdict


def dijkstra(graph, start):
    n = len(graph)
    dist = {i: float('inf') for i in range(1, n+1)}
    paths = defaultdict(list)
    dist[start] = 0
    paths[start] = [[]]
    min_heap = [(0, start)]

    while min_heap:
        current_dist, u = heapq.heappop(min_heap)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u]:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                paths[v] = [path + [v] for path in paths[u]]
                heapq.heappush(min_heap, (dist[v], v))
            elif dist[u] + weight == dist[v]:
                paths[v].extend([path + [v] for path in paths[u]])

    return dist, paths


def count_shortest_paths(paths, start, end):
    return len(paths[end])


def main():
    input_data = sys.stdin.read().split()
    N = int(input_data[0])
    M = int(input_data[1])
    S = int(input_data[2])
    E = int(input_data[3])

    graph = defaultdict(list)

    index = 4
    for _ in range(M):
        u = int(input_data[index])
        v = int(input_data[index+1])
        w = int(input_data[index+2])
        graph[u].append((v, w))
        graph[v].append((u, w))
        index += 3

    dist, paths = dijkstra(graph, S)

    shortest_paths_count = count_shortest_paths(paths, S, E)

    print(shortest_paths_count)


if __name__ == "__main__":
    main()
