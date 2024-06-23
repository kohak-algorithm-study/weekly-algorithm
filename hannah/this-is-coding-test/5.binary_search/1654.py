# https://www.acmicpc.net/problem/1654
# 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().rstrip().split())  # k는 이미 가지고 있는 랜선의 개수, n은 필요한 랜선의 개수
array = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

# array.sort()
start = 1
end = max(array)

max_h = 1
while True:
    count = 0
    if start > end:
        break

    h = (start + end) // 2

    for x in array:
        count += (x // h)

    if count >= n:
        if max_h < h:
            max_h = h
        start = h + 1
    else:
        end = h - 1

print(max_h)
