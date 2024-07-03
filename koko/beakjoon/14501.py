# i = 근무가능일수
# dp[i]  = 최대수익

import sys

n = int(input())

input_schedule_and_profit = []

for i in range(0, n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    input_schedule_and_profit.append((t, p))

input_schedule_and_profit.reverse()
input_schedule_and_profit.insert(0, [])

dp_table = [0] * (n+1)

for i in range(1, n+1):
    if i < input_schedule_and_profit[i][0]:
        dp_table[i] = dp_table[i-1]
    else:
        dp_table[i] = max(dp_table[i-1], dp_table[i - input_schedule_and_profit[i][0]] + input_schedule_and_profit[i][1])

print(dp_table[n])
