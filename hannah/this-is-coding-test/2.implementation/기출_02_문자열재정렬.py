'''
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력힙니다.
예를 들어 KIKA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

- 입력 조건
• 첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

- 출력 조건
• 첫째 줄에 문제에서 요구하는 정답을 출력합니다.

- 입력 예시1
K1KA5CB7
- 출력 예시1
ABCKK13

- 입력 예시2
AJKDLSI412K4JSJ9D
- 출력 예시2
ADDIJJJKKLSS20
'''

S = input()
a = ""
d = 0
for s in S:
    if s.isalpha():
        a += s
    else:
        d += int(s)

sorted_list = sorted(a)
print(''.join(sorted_list) + str(d))
