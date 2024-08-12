'''
https://www.acmicpc.net/problem/14888
'''
import sys


def dfs(depth, total, cnt_p, cnt_s, cnt_m, cnt_d):
    global max_value, min_value

    if depth == n:
        max_value = max(total, max_value)
        min_value = min(total, min_value)
        return

    if cnt_p > 0:
        dfs(depth + 1, total + nums[depth], cnt_p - 1, cnt_s, cnt_m, cnt_d)
    if cnt_s > 0:
        dfs(depth + 1, total - nums[depth], cnt_p, cnt_s - 1, cnt_m, cnt_d)
    if cnt_m > 0:
        dfs(depth + 1, total * nums[depth], cnt_p, cnt_s, cnt_m - 1, cnt_d)
    if cnt_d > 0:
        dfs(depth + 1, int(total / nums[depth]), cnt_p, cnt_s, cnt_m, cnt_d - 1)


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input().rstrip())
    nums = list(map(int, input().rstrip().split()))
    cnt_p, cnt_s, cnt_m, cnt_d = list(map(int, input().rstrip().split()))

    max_value = -1e9
    min_value = 1e9

    dfs(1, nums[0], cnt_p, cnt_s, cnt_m, cnt_d)

    print(max_value)
    print(min_value)
