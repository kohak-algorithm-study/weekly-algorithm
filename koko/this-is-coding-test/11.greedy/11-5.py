# 볼링공 고르기
n, m = map(int, input().split())
weight = list(map(int, input().split()))

answer = 0
for i in range(n-1):
    for j in range(i+1, n):
        if weight[i] != weight[j]:
            answer += 1

print(answer)
