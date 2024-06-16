'''
[숫자 카드 게임]
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다
룰은 다음과 같다

1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며 M은 열의 개수를 의미한다
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다
3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
4. 따라서 처음에 카드를 골라낼 행을 선택할 때
  이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다

예를 들어 3*3 형태로 카드들이 다음과 같이 놓여 있다고 가정하자
3 1 2
4 1 4
2 2 2

여기서 카드를 골라낼 행을 고를 때 첫 번째 혹은 두 번째 행을 선택하는 경우
최종적으로 뽑는 카드는 1이다.
하지만 세 번째 행을 선택하는 경우 최종적으로 뽑는 카드는 2이다.

따라서 이 예제에서는 세 번째 행을 선택하여 숫자 2가 쓰여진 카드를 뽑는 것이 정답이다.

카드들이 N x M 형태로 놓여 있을 때, 게임의 룰에 맞게 카드를 뽑는 프로그램을 만드시오
- 입력 조건
1 <= N, M <= 100
둘째줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10,000이하의 자연수이다.

- 출력 조건
첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
'''
import sys

n, m = map(int, sys.stdin.readline().split())

result = 0
for i in range(n):
    array = list(map(int, sys.stdin.readline().split()))
    min_value = min(array)
    if min_value > result:
        result = min_value

print(result)
