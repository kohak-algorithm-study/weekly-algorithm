'''
https://school.programmers.co.kr/learn/courses/30/lessons/68935
'''


def solution(n):
    if n < 3:
        return n

    reversed_3_base = ''
    while n >= 3:
        n, mod = divmod(n, 3)
        reversed_3_base += str(mod)

        if n < 3:
            reversed_3_base += str(n)
            break

    answer = 0
    n = len(reversed_3_base)
    for i in range(n):
        if int(reversed_3_base[i]) == 0:
            continue
        answer += int(reversed_3_base[i]) * 3**((n - 1) - i)
    return answer


def solution2(n):
    tmp = ''
    while n:  # n이 0이 되면 반복문 종료
        tmp += str(n % 3)
        n = n // 3
    return int(tmp, 3)  # tmp를 3진수로 간주하고 10진수로 변환
