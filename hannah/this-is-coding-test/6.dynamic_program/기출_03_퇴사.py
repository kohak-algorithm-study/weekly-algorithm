'''
https://www.acmicpc.net/problem/14501
'''
import sys

input = sys.stdin.readline
n = int(input())
info = [tuple(map(int, input().split())) for _ in range(n)]
max_income = 0


def calculate_max_income(today, total_income):
    # 시간복잡도: 2^15 (모든 상황에서 한다/안한다를 따지기 때문) (트리 형태)
    global n, max_income

    if today >= n:  # 재귀 함수 종료 조건
        max_income = max(total_income, max_income)  # max_income 값 갱신
        return

    # 오늘 상담 하는 경우
    # 단, 상담 종료 일이 퇴사일을 지나는 경우에는 상담 할 수 없음
    if today + info[today][0] <= n:
        calculate_max_income(today + info[today][0], total_income + info[today][1])

    # 오늘 상담하지 않는 경우 -> 다음날로 이동. 수익은 그대로
    calculate_max_income(today + 1, total_income)


# calculate_max_income(0, 0)
# print(max_income)


def dynamic_program():
    dp = [0] * (n + 1)  # dp[i]: i번째 일의 상담 결정 시, 최대 수익(단, 뒤부터 접근(dp[7] -> dp[6] -> dp[5] -> ...))
    for i in range(n - 1, -1, -1):
        required_days = info[i][0]
        i_income = info[i][1]

        # 상담 종료일이 퇴사일 이후면 상담 못함 -> 이전 값 그대로
        if i + required_days > n:
            dp[i] = dp[i + 1]
            continue

        # 상담 할때, 안할때 중 큰 값
        o = dp[i + required_days] + i_income
        x = dp[i + 1]
        dp[i] = max(o, x)

    print(dp[0])


dynamic_program()
