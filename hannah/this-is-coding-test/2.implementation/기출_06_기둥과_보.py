'''
https://school.programmers.co.kr/learn/courses/30/lessons/60061
'''


def check_column(installed, x, y):
    if y == 0:
        return True

    if [x - 1, y, 1] in installed or [x, y, 1] in installed:
        return True

    if [x, y - 1, 0] in installed:
        return True

    return False


def check_beam(installed, x, y):
    if y == 0:
        return False

    if [x, y - 1, 0] in installed or [x + 1, y - 1, 0] in installed:
        return True

    if [x - 1, y, 1] in installed and [x + 1, y, 1] in installed:
        return True

    return False


def check_delete_passible(installed):
    for x, y, is_beam in installed:
        if is_beam:
            result = check_beam(installed, x, y)
        else:
            result = check_column(installed, x, y)

        if not result:
            return False
    return True


def solution(n, build_frame):
    result = []
    for x, y, is_beam, is_for_install in build_frame:
        if is_for_install:  # 설치
            if is_beam:
                if not check_beam(result, x, y):
                    continue
            else:
                if not check_column(result, x, y):
                    continue

            result.append([x, y, is_beam])

        else:
            if [x, y, is_beam] in result:
                result.remove([x, y, is_beam])

            if not check_delete_passible(result):
                result.append([x, y, is_beam])

    return sorted(result)


# result = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
# print(result)
