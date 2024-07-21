import sys

n = int(input())
x = list(map(int, sys.stdin.readline().split()))

x.sort()

group = 0
group_cnt = 0
fear = 0

for i in range(len(x)):

    fear = x[i]
    group += 1

    if fear == group:
        group = 0
        peer = 0
        group_cnt += 1


print(group_cnt)


'''
5
2 3 1 2 2
'''

