# 모험가 길드 : 공포도를 오름차순으로 정렬한 뒤, 현재 모험가의 공포도와 멤버의 수가 동일하거나, 멤버가 더 많다면 그룹을 결성

n = int(input())
data = list(map(int, input().split()))

data.sort()

group = 0
member = 0

for x in data:
    member += 1
    if member >= x:
        group += 1
        member = 0

print(group)
