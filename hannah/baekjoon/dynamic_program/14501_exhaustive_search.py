'''
https://www.acmicpc.net/problem/14501
'''
# 완전 탐색으로 풀기

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
result = 0


def dfs(n, current_sum):  # n = 현재 날짜 + t, current_sum: 현재 날짜까지의 수익 합
    global result

    # 종료 조건
    if n >= N + 1:
        result = max(result, current_sum)
        return

    t, p = schedule[n - 1]

    # 해당 날짜에 상담하는 경우 (상담 종료일이 퇴사일 이전일때만 가능)
    if n + t <= N + 1:
        dfs(n + t, current_sum + p)

    # 상담하지 않는 경우
    dfs(n + 1, current_sum)


dfs(1, 0)
print(result)
