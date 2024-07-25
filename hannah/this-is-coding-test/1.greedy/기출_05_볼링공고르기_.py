'''
A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다.
또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주합니다.
볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.

예를 들어 N이 5이고, M이 3이며 각각의 무게가 차례대로 1, 3, 2, 3, 2일 때 각 공의 번호가 차례대로 1번부터 5번까지 부여됩니다.
이때 두 사람이 고를 수 있는 볼링공 번호의 조합을 구하면 다음과 같습니다.

(1번, 2번), (1번, 3번), (1번, 4번), (1번, 5번), (2번, 3번), (2번, 5번), (3번, 4번), (4번, 5번)
결과적으로 두 사람이 공을 고르는 경우의 수는 8가지입니다.

N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

- 입력 조건
• 첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.(1 <= N <= 1,000,  1 <= M <= 10)
• 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다. (1 <= K <= M)

- 출력 조건
• 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.

- 입력 예시1
5 3
1 3 2 3 2

- 출력 예시1
8

- 입력 예시2
8 5
1 5 4 3 2 4 5 2

- 출력 예시2
25

'''
from itertools import combinations

n, m = map(int, input().split())
bolls = list(map(int, input().split()))

combinations = list(combinations(bolls, 2))
result = len(combinations)
for com in combinations:
    if com[0] == com[1]:
        result -= 1


print(result)
