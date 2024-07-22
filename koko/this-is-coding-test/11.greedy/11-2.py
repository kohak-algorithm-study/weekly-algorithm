# 곱하기 혹은 더하기(단 모든 연산은 왼쪽에서부터 순서대로 이루어진다.)
# 0이나 1이먄 더하고 아니면 곱하고

s = input()

answer = 0

for i in s:
    if int(i) <= 1 or answer <= 1:
        answer += int(i)
    else:
        answer *= int(i)

print(answer)
