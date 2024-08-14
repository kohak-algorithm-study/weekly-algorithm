'''
https://www.acmicpc.net/problem/1715
'''
import heapq
import sys

input = sys.stdin.readline

n = int(input())
cards_cnt_q = [int(input()) for _ in range(n)]
heapq.heapify(cards_cnt_q)

result = 0
while len(cards_cnt_q) >= 2:
    node1 = heapq.heappop(cards_cnt_q)
    node2 = heapq.heappop(cards_cnt_q)
    sub_sum = node1 + node2
    result += sub_sum
    heapq.heappush(cards_cnt_q, sub_sum)

print(result)
