'''
https://school.programmers.co.kr/learn/courses/30/lessons/60063
'''
from collections import deque


def solution(board):
    answer = bfs(board)
    return answer


def get_next_positions(board, cur_pos):
    n = len(board)
    next_positions = []
    (x1, y1), (x2, y2) = cur_pos

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 상하좌우로 이동하는 경우
    for i in range(4):
        nx1 = x1 + dx[i]
        ny1 = y1 + dy[i]
        nx2 = x2 + dx[i]
        ny2 = y2 + dy[i]

        if nx1 < 0 or ny1 < 0 or nx2 >= n or ny2 >= n:
            continue

        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            next_positions.append(((nx1, ny1), (nx2, ny2)))

    # 현재 가로로 놓여있는 경우
    if x1 == x2:
        # 가로 -> 세로 (위로 회전)
        if x1 - 1 >= 0 and x2 - 1 >= 0:
            if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:  # 위에 두 칸 모두 0이여야 회전 가능
                next_positions.append(((x1 - 1, y1), (x1, y1)))
                next_positions.append(((x2 - 1, y2), (x2, y2)))

        # 가로 -> 세로 (아래로 회전)
        if x1 + 1 < n and x2 + 1 < n:
            if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:  # 아래 두 칸 모두 0이여야 회전 가능
                next_positions.append(((x1, y1), (x1 + 1, y1)))
                next_positions.append(((x2, y2), (x2 + 1, y2)))

    # 현재 세로로 놓여있는 경우
    else:
        # 세로 -> 가로 (오른쪽으로 회전)
        if y1 + 1 < n and y2 + 1 < n:
            if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:  # 오른쪽 두 칸 모두 0이여야 회전 가능
                next_positions.append(((x1, y1), (x1, y1 + 1)))
                next_positions.append(((x2, y2), (x2, y2 + 1)))

        # 세로 -> 가로 (왼쪽으로 회전)
        if y1 - 1 >= 0 and y2 - 1 >= 0:
            if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:  # 왼쪽 두 칸 모두 0이여야 회전 가능
                next_positions.append(((x1, y1 - 1), (x1, y1)))
                next_positions.append(((x2, y2 - 1), (x2, y2)))

    return next_positions


def bfs(board):
    n = len(board)
    visited = []
    pos = ((0, 0), (0, 1))
    cost = 0

    q = deque([(pos, cost)])
    visited.append(pos)

    while q:
        pos, cost = q.popleft()

        for next_pos in get_next_positions(board, pos):
            if next_pos not in visited:
                visited.append(next_pos)
                q.append((next_pos, cost + 1))

            if next_pos[1][0] == (n - 1) and next_pos[1][1] == (n - 1):
                return cost + 1

    return 0


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
