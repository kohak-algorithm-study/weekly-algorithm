def solution(s: str) -> int:
    prev_number = s[0]
    group_count = 1
    for number in s[1:]:
        if prev_number != number:
            prev_number = number
            group_count += 1

    return group_count // 2


print(solution('0001100'))  # 1
