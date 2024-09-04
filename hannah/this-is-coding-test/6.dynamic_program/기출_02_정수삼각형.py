'''
https://www.acmicpc.net/problem//1932
'''
import sys

input = sys.stdin.readline

n = int(input())
dp = []
for _ in range(n):
    data = list(map(int, input().strip().split()))
    data += [-1] * (n - len(data))
    dp.append(data)


for i in range(1, n):
    for j in range(n):
        if dp[i][j] == -1:
            continue

        dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + dp[i][j]

print(max(dp[-1]))
