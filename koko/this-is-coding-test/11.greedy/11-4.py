# 만들 수 없는 금액
# 화폐 단위가 작은 순서대로 동전을 확인하며,
# 현재 확인하는 동전을 이용해 max_coin 금액 또한 만들 수 있는지 확인
# 만약 max_coin 금액을 만들 수 있다면, max_coin 값을 업데이트하는(증가시키는) 방식을 이용
# 이러한 원리를 이용하면, 단순히 동전을 화폐 단위 기준으로 정렬한 뒤에, 
# 화폐 단위가 작은 동전부터 하나씩 확인하면서 max_coin 변수를 업데이트하는 방법으로 최적의 해를 계산


n = int(input())
coins = sorted(list(map(int, input().split())))

max_coin = 1
for coin in coins:
    if max_coin < coin:
        break
    max_coin += coin

print(max_coin)
