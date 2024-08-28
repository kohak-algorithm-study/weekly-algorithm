'''
https://www.acmicpc.net/problem/3190
'''
import sys

input = sys.stdin.readline
n = int(input())
k = int(input())

gragh = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().rstrip().split())
    gragh[x][y] = 1

move_n = int(input())
moves = {}
for _ in range(move_n):
    second, direction = input().rstrip().split()
    moves[int(second)] = direction

next_d_dict = {
    'ED': 'S',
    'EL': 'N',
    'SD': 'W',
    'SL': 'E',
    'WD': 'N',
    'WL': 'S',
    'ND': 'E',
    'NL': 'W'
}
move_by_d = {
    'E': (0, 1),
    'S': (1, 0),
    'W': (0, -1),
    'N': (-1, 0),
}


d = 'E'
s = 0
x, y = 1, 1
gragh[x][y] = 2
q = [(x, y)]  # 뱀이 현재 차지하고 있는 위치 저장
while True:
    s += 1

    nx = x + move_by_d[d][0]
    ny = y + move_by_d[d][1]

    if nx <= 0 or ny <= 0 or nx > n or ny > n:
        break

    if gragh[nx][ny] == 0:
        gragh[nx][ny] = 2
        q.append((nx, ny))

        px, py = q.pop(0)  # 이전 위치는 0으로 원복(꼬리 제거)
        gragh[px][py] = 0

    elif gragh[nx][ny] == 1:
        gragh[nx][ny] = 2
        q.append((nx, ny))

    else:
        break

    x, y = nx, ny

    if s in moves:
        d = next_d_dict[d + moves[s]]

print(s)
