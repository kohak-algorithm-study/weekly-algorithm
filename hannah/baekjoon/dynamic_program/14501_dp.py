'''
https://www.acmicpc.net/problem/14501
'''
# top-down

N = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(N)]
dp = [0] * (N + 2)  # dp[i] == i일차 까지의 최대 수익

# 뒤에서 부터 탐색
# dp[7]: 상담 불가능 -> 초기값 >> 0
# dp[6]: 상담 불가능 -> 7일차 값 그대로 >> 0
# dp[5]: 상담 가능 -> {상담O -> 0 + 15, 상담X -> 0(6일차 값 그대로)} 이 중 큰 값 >> 15
# dp[4]: 상담 가능 -> {상담O -> 4+t일차 값 + p = dp[5] + 20 = 35, 상담X -> 5일차 값 그대로 = 15} 이 중 큰 값 >> 35
# dp[3]: 상담 가능 -> {상담O -> 3+t일차 값 + p = dp[4] + 10 = 45, 상담X -> 4일차 값 그대로 = 35} 이 중 큰 값 >> 45
# dp[2]: 상담 가능 -> {상담O -> 2+t일자 값 + p = dp[7] + 20 = 20, 상담X -> 3일차 값 그대로 = 45} 이 중 큰 값 >> 45
# dp[1]: 상담 가능 -> {상담O -> 1+t일자 값 + p = dp[4] + 10 = 45, 상담X -> 2일차 값 그대로 = 45} 이 중 큰 값 >> 45
last_t, last_p = schedule[-1]

if last_t <= 1:
    dp[N] = last_p

for i in range(N - 1, 0, -1):  # 9, 8, 7, ..., 1
    t, p = schedule[i - 1]

    if i + t > N + 1:  # i일차에 상담을 했을 때, 퇴사일 안에 끝나지 않는다면 상담 불가 -> i + 1값 그대로
        dp[i] = dp[i + 1]
        continue

    dp[i] = max(dp[i + t] + p, dp[i + 1])

print(dp[1])
