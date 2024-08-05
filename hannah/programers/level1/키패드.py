'''
https://school.programmers.co.kr/learn/courses/30/lessons/67256
'''


def calculate_disc(target_loc, cur_loc):
    x = abs(target_loc[0] - cur_loc[0])
    y = abs(target_loc[1] - cur_loc[1])
    return x + y


def find_move_hand(hand, cur_r, cur_l, target_loc):
    right_disc = calculate_disc(target_loc, cur_r)
    left_disc = calculate_disc(target_loc, cur_l)

    if right_disc < left_disc:
        move_hand = "right"
    elif right_disc > left_disc:
        move_hand = "left"
    else:
        move_hand = "right" if is_right(hand) else "left"

    return move_hand


def is_right(hand):
    return True if hand == 'right' else False


def solution(numbers, hand):
    answer = ''
    right_num = {3, 6, 9}
    left_num = {1, 4, 7}

    map = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1),
    }

    cur_r = (3, 2)
    cur_l = (3, 0)
    for num in numbers:
        if num in right_num:
            answer += 'R'
            cur_r = map[num]
        elif num in left_num:
            answer += 'L'
            cur_l = map[num]
        else:
            move_hand = find_move_hand(hand, cur_r, cur_l, map[num])
            if is_right(move_hand):
                answer += 'R'
                cur_r = map[num]
            else:
                answer += 'L'
                cur_l = map[num]

    return answer
