import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())

gragh = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gragh[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

queue = deque([x])
while queue:
    now = queue.popleft()
    for next in gragh[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            queue.append(next)


check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)


# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4