'''
https://school.programmers.co.kr/learn/courses/30/lessons/60057
'''


def solution(s):
    min_len = len(s)

    for i in range(1, len(s) // 2 + 1):  # 압축 자리수(반복 횟수는 최대 len(s)의 반값까지 가능하다)
        repeat_cnt = 1
        new_str = ''
        for j in range(0, len(s), i):  # 인덱스
            a = s[j: (j + i)]
            b = s[(j + i): (j + i + i)]

            if a == b:
                repeat_cnt += 1
            else:
                if repeat_cnt == 1:
                    new_str += a
                else:
                    new_str += str(repeat_cnt) + a
                repeat_cnt = 1

        if len(new_str) < min_len:
            min_len = len(new_str)
    return min_len


result = solution("abcabcabcdabcfabcabcabczabcabcdddabc")

print(f'result: {result}')
