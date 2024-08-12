'''
https://www.acmicpc.net/problem/18428
'''
# 시간초과!!

import sys
from itertools import combinations

input = sys.stdin.readline
n = int(input())
gragh = [list(input().rstrip().split()) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(n) if gragh[i][j] == 'X']   # 장애물을 설치 할 수 있는 곳
teachers = [(i, j) for i in range(n) for j in range(n) if gragh[i][j] == 'T']  # 선생님 위치 저장

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def avoid_observation():

    for combi in combinations(empty, 3):  # 장애물 위치 조합
        for x, y in combi:
            gragh[x][y] = 'O'

        if not find_student(gragh):  # 선생님이 학생을 찾지 못하면 감시 피하기 성공
            return True

        # 장애물 원상복구(백트래킹)
        for x, y in combi:
            gragh[x][y] = 'X'

    return False


def find_student(o_map):
    # 한 선생님 당 한 방향으로만(=일직선으로만) 탐색 해야함
    for teacher_x, teacher_y in teachers:
        for i in range(4):
            x = teacher_x + dx[i]
            y = teacher_y + dy[i]

            while True:

                if x < 0 or y < 0 or x >= n or y >= n:
                    break  # 이쪽 방향으로는 탐색 끝. 다음 방향 진행

                # 학생을 만나면 종료(True 반환)
                if o_map[x][y] == 'S':
                    return True

                # 장애물을 만나면 이 방향으로는 학생 찾기에 실패한 것이므로 이 방향은 탐색 끝
                if o_map[x][y] == 'O':
                    break  # 이쪽 방향으로는 탐색 끝. 다음 방향 진행

                if o_map[x][y] == 'X':
                    # 위치 갱신
                    x += dx[i]
                    y += dy[i]


avoid_result = avoid_observation()


if avoid_result:  # 감시피하기 성공
    print("YES")
else:
    print("NO")
