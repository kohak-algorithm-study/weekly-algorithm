'''
https://www.acmicpc.net/problem/18353
'''
# 가장 긴 증가하는 부분 수열(LIS)

n = int(input())
data = list(map(int, input().split()))
dp = [1] * n  # dp[i]: data[i]를 마지막 원소로 가지는 부분 수열의 최대 길이. 최소 자기 자신 하나로만 부분수열을 가질 수 있으므로 1로 초기화한다.

for i in range(1, n):
    for j in range(i):
        if data[i] < data[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(n - max(dp))
