'''
못생긴 수란 오직 2, 3, 5만을 소인수(Prime Factor)로 가지는 수를 의미합니다.
다시 말해 오직 2, 3, 5를 약수로 가지는 합성수를 의미합니다. 1은 못생긴 수라고 가정합니다.
따라서 못생긴 수들은 {1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, ..} 순으로 이어지게 됩니다.
이때, n번째 못생긴 수를 찾는 프로그램을 작성하세요.
예를 들어 11번째 못생긴 수는 15입니다.
단, n은 1이상 1,000이하

[입력 예시1]
10
[출력 예시1]
12

[입력 예시2]
4
[출력 예시2]
4
'''
n = int(input())
ugly_nums = [0] * n
ugly_nums[0] = 1

next2, next3, next5 = 2, 3, 5
x2, x3, x5 = 0, 0, 0  # x번째 2의 배수의 x값
for i in range(1, n):
    ugly_nums[i] = min(next2, next3, next5)

    if ugly_nums[i] == next2:
        x2 += 1
        next2 = ugly_nums[x2] * 2
    elif ugly_nums[i] == next3:
        x3 += 1
        next3 = ugly_nums[x3] * 3
    else:
        x5 += 1
        next5 = ugly_nums[x5] * 5
