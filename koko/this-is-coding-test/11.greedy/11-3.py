# 문자열 뒤집기
S = list(map(int, input()))

count_zero = 0
count_one = 0
first_count = S[0]
for s in S:
    if s == 1 and first_count == 1:
        count_one += 1
        first_count = 0
    elif s == 0 and first_count == 0:
        count_zero += 1
        first_count = 1

print(min(count_zero, count_one))
