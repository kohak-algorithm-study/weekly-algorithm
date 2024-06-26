'''
[두 배열의 원소 교체]
동빈이는 두 개의 배열 A와 B를 가지고 있다. 
두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수이다.
동빈이는 최대 K번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 
배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말한다.
동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이다.

N, K, 그리고 배열 A와 B의 정보가 주어졌을 때,
최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하시오.

예를 들어 N = 5, K = 3이고 배열 A와 B가 다음과 같다고 하자

• 배열 A = [1, 2, 5, 4, 3]
• 배열 B = [5, 5, 6, 6, 5]

이 경우, 다음과 같이 세 번의 연산을 수행할 수 있다.
• 연산 1) 배열 A의 원소 ‘1’과 배열 B의 원소 ‘6’을 바꾸기
• 연산 2) 배열 A의 원소 ‘2’와 배열 B의 원소 ‘6’을 바꾸기
• 연산 3) 배열 A의 원소 ‘3’과 배열 日의 원소 ‘5’를 바꾸기

세 번의 연산 이후 배열 A와 배열 B의 상태는 다음과 같이 구성될 것이다.
• 배열 A = [6, 6, 5, 4, 5]
• 배열 B = [3, 5, 1, 2, 5]
이때 배열 A의 모든 원소의 합은 26 이 되며, 이보다 더 합을 크게 만들 수는 없다.
따라서 이 예시의 정답은 26이 된다.


입력 조건
- 첫 번째줄에 N, K가공백으로 구분되어 입력된다. (1 < N < 100,000, 0 < K < N)
- 두 번째 줄에 배열 A의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000 보다 작은 자연수이다.
- 세 번째 줄에 배열 B의 원소들이 공백으로 구분되어 입력된다. 모든 원소는 10,000,000 보다 작은 자연수이다.
'''
# 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 한다. (N²이면 안됨)
# A는 오름차순, B는 내림차순으로 정렬해서, A에서 가장 작은 수와, B에서 가장 큰 수를 바꾼다.

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))
b = list(map(int, sys.stdin.readline().rstrip().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break  # 두 값이 같아진 시점부터는 값을 바꾸면 오히려 배열a의 원소 합이 작아진다

print(sum(a))