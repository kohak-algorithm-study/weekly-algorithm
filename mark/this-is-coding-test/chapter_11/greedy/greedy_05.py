import sys

n, m = map(int, input().split())
k = list(map(int, sys.stdin.readline().split()))


cnt = 0
for i in range(len(k)):
    for j in range(i+1, len(k)):

       if k[i] == k[j]:
           continue

       else:
           cnt += 1

print(cnt)