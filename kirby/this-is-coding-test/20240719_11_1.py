def solution(arr: list) -> int:
    answer = 0
    group = []

    arr.sort()

    for x in arr:
        group.append(x)
        if len(group) >= x:
            answer += 1
            group.clear()

    return answer


print(solution([2, 3, 1, 2, 2]))  # 2
