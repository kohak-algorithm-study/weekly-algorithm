'''
https://school.programmers.co.kr/learn/courses/30/lessons/60059
'''
import copy


def rotate_key(key):
    n = len(key)
    rotated_key = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_key[j][n - i - 1] = key[i][j]

    return rotated_key


def solve_lock(lock, wide_lock, start_x, start_y, key, n, m):
    copy_lock = copy.deepcopy(lock)
    for i in range(m):
        for j in range(m):
            if m <= start_x + i < (n + m) and m <= start_y + j < (n + m):
                # if wide_lock[start_x + i][start_y + j] == 1 and key[i][j] == 1:  # 둘다 돌기면 실패
                #     return False
                # if wide_lock[start_x + i][start_y + j] == 0 and key[i][j] == 1:
                #     copy_lock[start_x + i - m][start_y + j - m] = 1
                copy_lock[start_x + i - m][start_y + j - m] = wide_lock[start_x + i][start_y + j] ^ key[i][j]

    has_zero = any(0 in row for row in copy_lock)

    return False if has_zero else True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    wide_lock = [[0] * (n + 2 * m) for _ in range(n + 2 * m)]
    for i in range(n):
        for j in range(n):
            wide_lock[m + i][m + j] = lock[i][j]

    for _ in range(4):  # 90도 회전해서 4가지
        key = rotate_key(key)

        # 1칸이라도 겹쳐있어야하므로 key의 제일 첫 칸이 wide_lock의 (1, 1)여야하고 또는 제일 끝 칸이 (n+2m-1, n+2m-1)여야 한다.
        # 제일 끝 칸이 (n+2m-1, n+2m-1)이라는 것은 그 때의 key의 첫 칸이 (n+m-1, n+m-1)일때다.
        # 그래서 wide_lock의 (i, j) 범위를 (1, 1) ~ (n+m-1, n+m-1)로 잡음
        for i in range(1, n + m):
            for j in range(1, n + m):
                solved = solve_lock(lock, wide_lock, i, j, key, n, m)
                if solved:
                    return True

    return False


result = solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
print(result)
