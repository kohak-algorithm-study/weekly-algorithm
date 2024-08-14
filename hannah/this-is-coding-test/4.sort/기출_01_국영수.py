'''
https://www.acmicpc.net/problem/10825
'''
import sys

input = sys.stdin.readline
n = int(input())
students = []
for _ in range(n):
    name, k, e, m = list(input().rstrip().split())
    students.append((name, int(k), int(e), int(m)))


ordered = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in ordered:
    print(x[0])
