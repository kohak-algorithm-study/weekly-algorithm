'''
https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''


def solution(N, stages):
    total_player = len(stages)
    failure_rate = {}
    for stage_num in range(1, N + 1):
        if total_player != 0:
            cnt = stages.count(stage_num)
            failure_rate[stage_num] = cnt / total_player

            total_player -= cnt  # 다음 단계의 도전자 수는 총 도전자 수에서 이번 단계를 통과하지 못한 도전자 수를 뺀 값
        else:
            failure_rate[stage_num] = 0

    # answer_dict = sorted(failure_rate.items(), key = lambda x: (-x[1], x[0]))
    # answer = [k for k, v in answer_dict]

    return sorted(failure_rate, key=lambda key: -failure_rate[key])


result1 = solution([2, 1, 2, 6, 2, 4, 3, 3])  # [3,4,2,1,5]
result2 = solution([4, 4, 4, 4, 4])  # [4,1,2,3]
