'''
[성적이 낮은 순서로 학생 출력하기]
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오

입력 조건 
- 첫 번째 줄에 학생의 수 N이 입력된다(1 < N < 100,000)
- 두 번째 줄부터 N + 1번째 줄에는 학생의 이름을 나타내는 문자열 A와 학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다
- 문자열 A의 길이와 학생의 성적은 100이하의 자연수이다

출력 조건
- 모든 학생의 이름을 성적이 낮은 순서대로 출력*E 성적이 동일한 학생들의 순서는 자유롭게 출력해도 괜찮다.
'''

# 학생 수가 최대 100,000이므로 최악의 경우 O(NlogN)인 알고리즘을 이용하거나, O(N)을 보장하는 계수 정렬을 이용하면 된다.

import sys

n = int(sys.stdin.readline().rstrip())
array = []
for i in range(n):
    name, grade_str = sys.stdin.readline().rstrip().split()
    array.append((int(grade_str), name))
    
array.sort()

for student in array:
    print(student[1], end=' ')

# print(*array)