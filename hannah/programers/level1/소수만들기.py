'''
https://school.programmers.co.kr/learn/courses/30/lessons/12977
'''
from itertools import combinations


def check_prime_number(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    else:
        return True


# 루트를 이용하여 탐색 범위를 줄일 수 있는 이유:
# 합성수 x = a * b 일때, a와 b 중 하나는 무조건 squr(x)보다 작거나 같다.
def check_prime_number_2(number):
    for i in range(2, int(number ** 0.5) + 1):  # **0.5는 루트를 의미
        if number % i == 0:
            return False
    else:
        return True


def solution(nums):
    answer = 0
    for combi in combinations(nums, 3):
        if check_prime_number(sum(combi)):
            answer += 1
    return answer
