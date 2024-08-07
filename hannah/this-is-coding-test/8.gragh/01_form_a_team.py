'''
[팀 결성]
학교에서 학생들에게 0번부터 이번까지의 번호를 부여했다.
처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N 十 1개의 팀이 존재한다.
이때 선생님은 ‘팀 합치기’ 연산과 ‘같은 팀 여부 확인’ 연산을 사용할 수 있다

1. ‘팀 합치기’ 연산은 두 팀을 합치는 연산이다.
2. ‘같은 팀 여부 확인’ 연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.

선생님이 M개의 연산을 수행할 수 있을 때, ‘같은 팀 여부 확인’ 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.

- 입력 조건
• 첫째 줄에 N, M이 주어진다. M은 입력으로 주어지는 연산의 개수이다
• 다음 M개의 줄에는 각각의 연산이 주어진다.
• ‘팀 합치기’ 연산은 O a b 형태로 주어진다.  이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
• ‘같은 팀 여부 확인’ 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다.
• a와 b는 N 이하의 양의 정수이다

- 출력 조건
• ‘같은 팀 여부 확인’ 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.

- 입력예시
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

- 출력예시
NO
NO
YES
'''


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    root_of_a = find_parent(parent, a)
    root_of_b = find_parent(parent, b)

    if root_of_a < root_of_b:
        parent[root_of_b] = root_of_a
    else:
        parent[root_of_a] = root_of_b


N, M = map(int, input().split())
parent = [0] * (N + 1)
find_result = []
for i in range(1, N + 1):
    parent[i] = i

for _ in range(M):
    operation, a, b = map(int, input().split())

    if operation == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            find_result.append("YES")
        else:
            find_result.append("NO")


for result in find_result:
    print(result)
