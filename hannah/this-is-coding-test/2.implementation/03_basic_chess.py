'''
왕실 정원은  체스판과 같은 8*8 좌표 평면이다. 왕실 정원의 특정한 한 칸에 나이트가 서 있다.
나이트는 이동할 때는 L자 형태로만 이동할 수 있으며 정원 밖으로는 나갈 수 없다.

나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.
1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

이처럼 8*8 좌표 평면상에서 자이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램을 작성하시오.

이때 왕실의 정원에서 행 위치를 표현할 때는 1부터 8로 표현하며, 열 위치를 표현할 때는 a부터 h로 표현한다.

예를 들어 만약 나이트가 a1에 있을 때 이동할 수 있는 경우의 수는 다음 2가지이다.
1. 오른쪽으로 두 칸 이동 후 아래로 한 칸 이동 (c2)
2. 아래로 두 칸 이동 후 오른쪽으로 한 칸 이동 (b3)
a1의 위치는 좌표 평면에서 구석의 위치에 해당하며 나이트는 정원의 밖으로는 나갈 수 없기 때문이다.
'''

loc = input()
c = ord(loc[0]) - ord('a') + 1
r = int(loc[1])

# 2R+1D, 2R+1U, 2L+1D, 2L+1U
# 2U+1R, 2U+1L, 2D+1R, 2D+1L
# dx = [2, 2, -2, -2, 1, -1, 1, -1]
# dy = [1, -1, 1, -1, 2, 2, -2, -2]

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

cnt = 0
for step in steps:
    if (1 <= (c + step[0]) <= 8) and (1 <= (r + step[1]) <= 8):
        cnt += 1

print(cnt)
