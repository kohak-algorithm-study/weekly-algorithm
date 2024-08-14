'''
https://www.acmicpc.net/problem/18310
'''
# 순서대로 정렬했을 때 가운데 있는 집이 정답 -> 중앙값
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
mid_house = houses[(n - 1) // 2]
print(mid_house)
