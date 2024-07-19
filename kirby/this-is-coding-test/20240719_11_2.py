def solution(s: str) -> int:
    answer = 0
    numbers = list(map(int, s))

    answer = numbers[0]
    for number in numbers[1:]:
        answer = max(answer + number, answer * number)

    return answer


print(solution('02984'))  # 576
print(solution('567'))  # 210
