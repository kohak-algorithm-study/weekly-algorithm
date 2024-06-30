# DP - 탑다운 방식: 재귀함수 사용 -> O(N)
# 피보나치 수열 - 99번째 피보나치 수열 구하기
dp = [0] * 100


def fibo(x):
    if x == 1 or x == 2:
        return 1

    if dp[x] != 0:
        return dp[x]

    dp[x] = fibo(x - 1) + fibo(x - 2)
    return dp[x]


print(fibo(99))
