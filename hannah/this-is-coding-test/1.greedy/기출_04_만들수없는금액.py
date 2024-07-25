'''
동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다.
이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.
예를 들어, N = 5이고, 각 동전이 각각 3원, 2원, 1원, 1원, 9원짜리 （화폐 단위） 동전이라고 가정합시다.
이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 8원입니다.
또 다른 예시로, N = 3이고, 각 동전이 각각 3원, 5원, 7원짜리 （화폐 단위） 동전이라고 가정합시다.
이때 동빈이가 만들 수 없는 양의 정수 금액 중 최솟값은 1원입니다.

- 입력 조건
• 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N 이 주어집니다. (1 <= N <= 1,000)
• 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다.
  이때, 각 화폐 단위는 1,000,000 이하의 자연수입니다.

- 출력 조건
• 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액중 최솟값을 출력합니다.
'''
from itertools import combinations

n = int(input())
coins = list(map(int, input().split()))

coins.sort()


def find_sum_combinations():
    sum_combinations = set()

    for i in range(1, len(coins) + 1):
        for com in combinations(coins, i):
            sum_combinations.add(sum(com))
    return sum_combinations


sum_combinations = find_sum_combinations()


def find_min_x():
    for x in range(1, coins[-1] + 1):
        if x < coins[0]:
            return x

        if x not in sum_combinations:
            return x


print(find_min_x())
