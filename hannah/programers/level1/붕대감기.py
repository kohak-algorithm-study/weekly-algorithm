def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health
    last_attack_s = attacks[-1][0]

    desc_attacks = sorted(attacks, reverse=True)
    attack = desc_attacks.pop()

    consecutive_s = 0
    for s in range(1, last_attack_s + 1):
        if s == attack[0]:  # 공격 당함
            health -= attack[1]
            consecutive_s = 0
            if desc_attacks:
                attack = desc_attacks.pop()
        else:
            health += x
            consecutive_s += 1

            if consecutive_s == t:
                consecutive_s = 0
                health += y

            if health > max_health:
                health = max_health

        if health <= 0:
            return -1

    return health


solution([1, 1, 1], 5, [[1, 2], [3, 2]])
