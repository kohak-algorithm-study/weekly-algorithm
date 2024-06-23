
# 4 11
# 802
# 743
# 457
# 539

k, n = map(int, input().split())
lan_lengths = [int(input()) for _ in range(k)]


start = 1
end = max(lan_lengths)

result = 0

while start <= end:
    mid = (start + end) // 2
    total = 0

    for length in lan_lengths:
        total += length // mid

    if total >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)