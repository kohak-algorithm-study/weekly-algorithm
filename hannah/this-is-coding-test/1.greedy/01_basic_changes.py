# 거스름돈 문제
# 거스름돈 500, 100, 50, 10원이 무한히 존재
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.

n = 1260
count = 0

changes = [500, 100, 50, 10]

for change in changes:
    count += n // change  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    n %= change  # 해당 화폐로 거슬러 주고 남은 돈

print(count)
