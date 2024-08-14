'''
https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''


def solution(N, stages):
    player_cnt = len(stages)

    failure_rate = {}
    for i in range(1, N + 1):
        stage_player_cnt = stages.count(i)
        if player_cnt <= 0:
            failure_rate[i] = 0
        else:
            failure_rate[i] = stage_player_cnt / player_cnt

        player_cnt -= stage_player_cnt

    print(failure_rate)
    return sorted(failure_rate, key=lambda key: -failure_rate[key])


# result = solution(4, [4, 4, 4, 4, 4])
# print(result)