# DP - 보텀업 방식: 반복문 사용
# 피보나치 수열 - 99번째 피보나치 수열 구하기
dp = [0] * 100
dp[1] = 1
dp[2] = 1

for i in range(3, 100):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[99])
