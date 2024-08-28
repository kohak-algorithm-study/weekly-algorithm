'''
https://school.programmers.co.kr/learn/courses/30/lessons/60063
'''
from collections import deque


def get_passible_next_position(board, x1, y1, x2, y2):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(board)

    positions = []

    # 이동하는 경우
    for i in range(4):
        nx1, ny1 = x1 + dx[i], y1 + dy[i]
        nx2, ny2 = x2 + dx[i], y2 + dy[i]

        if nx1 < 0 or ny1 < 0 or nx2 >= n or ny2 >= n:
            continue

        if board[nx1][ny1] == 0 and board[nx2][ny2] == 0:
            positions.append(((nx1, ny1), (nx2, ny2)))

    # 회전하는 경우
    if x1 == x2:  # 로봇이 가로로 놓여져 있을 때
        # 위쪽으로 돌려서 회전 할 때 -> 현재 두 칸의 윗 칸 모두가 0이여야 회전 가능
        if x1 - 1 >= 0 and x2 - 1 >= 0:
            if board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
                positions.append(((x1 - 1, y1), (x1, y1)))
                positions.append(((x2 - 1, y2), (x2, y2)))

        # 아래쪽으로 돌려서 회전 할 때 -> 현재 두 칸의 아랫 칸 모두가 0이여야 회전 가능
        if x1 + 1 < n and x2 + 1 < n:
            if board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                positions.append(((x1, y1), (x1 + 1, y1)))
                positions.append(((x2, y2), (x2 + 1, y2)))

    else:  # 로봇이 세로로 놓여져 있을 때
        # 오른쪽으로 돌려서 회전 할 때 -> 현재 두 칸의 오른쪽 칸 모두가 0이여야 회전 가능
        if y1 + 1 < n and y2 + 1 < n:
            if board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
                positions.append(((x1, y1), (x1, y1 + 1)))
                positions.append(((x2, y2), (x2, y2 + 1)))

        # 왼쪽으로 돌려서 회전 할 때 -> 현재 두 칸의 왼쪽 칸 모두가 0이여야 회전 가능
        if y1 - 1 >= 0 and y2 - 1 >= 0:
            if board[x1][y1 - 1] == 0 and board[x2][y2 - 1] == 0:
                positions.append(((x1, y1 - 1), (x1, y1)))
                positions.append(((x2, y2 - 1), (x2, y2)))

    return positions


def solution(board):
    step = 0
    positions = [((0, 0), (0, 1), step)]
    q = deque(positions)
    visited = []
    n = len(board)

    while q:
        (x1, y1), (x2, y2), step = q.popleft()
        if x2 == n - 1 and y2 == n - 1:
            break

        next_positions = get_passible_next_position(board, x1, y1, x2, y2)
        for np in next_positions:
            if np in visited:
                continue
            q.append((np[0], np[1], step + 1))
            visited.append(np)

    return step


result = solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])
print(result)
