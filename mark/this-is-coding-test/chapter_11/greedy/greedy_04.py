import sys

n = int(input())
coin_list = list(map(int, sys.stdin.readline().split()))

coin_list.sort()

money_list = []

target = 1
for coin in coin_list:

    if coin > target :
        break
    target += coin

print(target)

