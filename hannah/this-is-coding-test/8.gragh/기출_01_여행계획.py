'''
한울이가 사는 나라에는 N개의 여행지가 있으며, 각 여행지는 1 〜 N번까지의 번호로 구분됩니다.
또한 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있습니다.

이때, 여행지가 도로로 연결되어 있다면 양방향으로 이동이 가능하다는 의미입니다.
한울이는 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하고자 합니다.
예를 들어 N = 5 이고, 다음과 같이 도로의 정보가 주어졌다고 가정합시다.

• 1번 여행지 - 2번 여행지
• 1번 여행지 - 4번 여행지
• 1번 여행지 - 5번 여행지
• 2번 여행지 - 3번 여행지
• 2번 여행지 - 4번 여행지

만약 한울이의 여행 계획이 2번 -> 3번 -> 4번 -> 3번이라고 해봅시다.
이 경우 2번 -> 3번 -> 2번 -> 4번 -> 2번 -> 3번의 순서로 여행지를 방문하면, 여행 계획을 따를 수 있습니다.

여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때, 한울이의 여행 계획이 가능한지의 여부를 판별하는 프로그램을 작성하세요.

- 입력 조건
• 첫째 줄에 여행지의 수 N과 여행 계획에 속한 도시의 수 M이 주어집니다. (1 <= N, M <= 500)
• 다음 N개의 줄에 걸쳐 N x N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지의 여부가 주어집니다.
  그 값이 1이라면 서로 연결되었다는 의미이며, 0이라면 서로 연결되어 있지 않다는 의미입니다.
• 마지막 줄에 한울이의 여행 계획에 포함된 여행지의 번호들이 주어지며 공백으로 구분합니다.

- 출력 조건
• 첫째 줄에 한울이의 여행 계획이 가능하다면 YES를, 불가능하다면 NO를 출력합니다.

- 입력 예시
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3

- 출력 예시
YES
'''
'''
[문제 해설]
여행 계획에 포함된 도시들이 같은 집합에 속해있는지를 확인하면 된다. -> 서로소 집합 자료구조의 union 연산을 통해 부모노드가 같은지를 확인

'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n + 1)  # 부모노드 초기화
for i in range(1, n + 1):
    parent[i] = i  # 초기 부모 노드는 자기 자신으로 초기화


# 루트 노드 찾기
def find_parent(parent: list, x: int) -> int:
    if parent[x] != x:  # 현재 부모가 자기 자신이 아니라면 (= 루트 노드가 아니라는 의미)
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a_parent = find_parent(parent, a)
    b_parent = find_parent(parent, b)

    if a_parent < b_parent:
        parent[b] = a
    else:
        parent[a] = b


# 연결된 노드들은 union 연산 수행
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            union(parent, i + 1, j + 1)

plan = list(map(int, input().split()))

result = True
for i in range(1, m):
    a, b = plan[i - 1], plan[i]
    if find_parent(parent, a) != find_parent(parent, b):
        result = False

if result:
    print("YES")
else:
    print("NO")
