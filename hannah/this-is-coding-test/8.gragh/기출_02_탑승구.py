# 비슷한 문제: https://www.acmicpc.net/problem/10775
'''
공항에는 G개의 탑승구가 있으며, 각각의 탑승구는 1번부터 G번까지의 번호로 구분됩니다.
공항에는 P개의 비행기가 차례대로 도착할 예정이며, i번째 비행기를 1번부터 gi번째(1 <= gi <= G) 탑승구 중 하나에 영구적으로 도킹해야 합니다.
이때, 다른 비행기가 도킹하지 않은 탑승구에만 도킹할 수 있습니다.
또한 P개의 비행기를 순서대로 도킹하다가 만약에 어떠한 탑승구에도 도킹할 수 없는 비행기가 나오는 경우, 그 시점에서 공항의 운행을 중지합니다.
공항의 관리자는 최대한 많은 비행기를 공항에 도킹하고자 합니다.
비행기를 최대 몇 대 도킹할 수 있는지를 출력하는 프로그램을 작성하세요.

[입력 조건]
• 첫째 줄에는 탑승구의 수 G(1 <= G <= 100,000)가 주어집니다.
• 둘째 줄에는 비행기의 수 P(1 <= P <= 100,000)가 주어집니다.
• 다음 P개의 줄에는 각 비행기가 도킹할 수 있는 탑승구의 정보 gi(1 <= gi <= G)가 주어집니다.
  이는 i번째 비행기가 1번부터 gi번째(1 <= gi <= G) 탑승구 중 하나에 도킹할수 있다는 의미입니다.

[출력 조건]
• 첫째 줄에 도킹할 수 있는 비행기의 최대 개수를 출력합니다.

[입력 예시 1]
4
3
4
1
1

[출력 예시 1]
2

[입력 예시 2]
4
6
2
2
3
3
4
4

[출력 예시 2]
3

[입출력 예시에 대한 설명]
첫 번째 예시에서는 2번 비행기 혹은 3번 비행기를 1번 탑승구에 도킹하고 1번 비행기는 2번, 3번, 4번 탑승구 중 하나에 도킹할 때 최댓값을 가집니다.
두 번째 예시에서는 1번 비행기와 2번 비행기를 각각 1번 탑승구와 2번 탑승구에 도킹한 뒤에, 3번 비행기는 3번 탑승구에 도킹할 수 있습니다.
하지만 4번 비행기는 어떤 탑승구에도 도킹할 수 없기 때문에, 이 시점에서 공항의 운행이 중지됩니다.
'''
import sys

input = sys.stdin.readline

g = int(input())
p = int(input())
gates = [[] * (g + 1)]
input_data = [int(input()) for _ in range(p)]

# 루트 노드 초기화
parent = [0] * (g + 1)
for i in range(1, g + 1):
    parent[i] = i


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


# 도킹하는 과정 = 탑승구 간 합집합 연산 -> 왼쪽 노드와 합집합 연산 수행
result = 0
for x in input_data:
    root = find_parent(parent, x)  # 현재 비행기의 탑승구의 루트 확인
    if root == 0:
        break

    union_parent(parent, root, root - 1)
    result += 1

print(result)
