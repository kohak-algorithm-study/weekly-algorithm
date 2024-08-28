'''
https://school.programmers.co.kr/learn/courses/30/lessons/60060
'''
from collections import defaultdict


def binary_search_left(words, query_with_a):
    start = 0
    end = len(words) - 1

    left_idx = -1
    while start <= end:
        mid = (start + end) // 2

        if words[mid] == query_with_a:
            return mid

        elif words[mid] > query_with_a:
            end = mid - 1
            left_idx = mid
        else:
            start = mid + 1

    return left_idx


def binary_search_right(words, query_with_z):
    start = 0
    end = len(words) - 1

    right_idx = -1
    while start <= end:
        mid = (start + end) // 2
        if words[mid] == query_with_z:
            return mid
        elif words[mid] < query_with_z:
            start = mid + 1
            right_idx = mid
        else:
            end = mid - 1
    return right_idx


def count_by_range(words, query_with_a, query_with_z):
    left_idx = binary_search_left(words, query_with_a)  # bisect_left(words, query_with_a)

    if left_idx == -1:
        return 0

    right_idx = binary_search_right(words, query_with_z)  # bisect_right(words, query_with_z)
    return right_idx - left_idx + 1


def solution(words, queries):
    answer = []

    words_by_length = defaultdict(list)
    reversed_words_by_length = defaultdict(list)

    # 단어 length별로 단어 리스트 만들기
    for word in words:
        words_by_length[len(word)].append(word)
        reversed_words_by_length[len(word)].append(word[::-1])

    # 단어 length별 각 배열을 오름차순로 정렬
    for words in words_by_length.values():
        words.sort()

    for words in reversed_words_by_length.values():
        words.sort()

    for query in queries:
        cnt = 0
        if query[0] != '?':  # "?"가 접미사로 붙는 경우 -> 원래 단어 방향을 대상으로 탐색
            search_target_data = words_by_length[len(query)]
            # fro??? -> froaaa와 frozzz 사이에 해당되는 단어 개수를 구하기
            cnt = count_by_range(search_target_data, query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            search_target_data = reversed_words_by_length[len(query)]
            # ???o -> aaao와 zzzo 사이에 해당되는 단어 개수를 구하기
            cnt = count_by_range(search_target_data, query.replace('?', 'a')[::-1], query.replace('?', 'z')[::-1])

        answer.append(cnt)

    return answer


result = solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"])
print(result)
