'''
https://school.programmers.co.kr/learn/courses/30/lessons/17682
'''
import re


def calculrate_bonus(score, bonus_type):
    if bonus_type == 'S':
        return score
    if bonus_type == 'D':
        return score ** 2
    return score ** 3


def calculrate_option(scores, option_type):
    if option_type == '*':
        if len(scores) >= 2:
            score1 = scores.pop()
            score2 = scores.pop()
            scores.append(score2 * 2)
            scores.append(score1 * 2)
        else:
            score = scores.pop()
            scores.append(score * 2)
    else:
        score = scores.pop()
        scores.append(-score)

    return scores


def solution(dartResult):
    scores = []
    dart_results = re.findall(r'\d+[^\d]*', dartResult)

    for dart_result in dart_results:
        if dart_result[1].isdigit():
            num = int(dart_result[:2])
            rest = dart_result[2:]
        else:
            num = int(dart_result[0])
            rest = dart_result[1:]

        scores.append(calculrate_bonus(num, rest[0]))
        if len(rest) == 2:
            scores = calculrate_option(scores, rest[-1])

    return sum(scores)


# result = solution("1S2D*3T")
# result = solution("1D2S#10S")
result = solution("1D2S0T")
# result = solution("1S*2T*3S")
# result = solution("1D#2S*3S")

print(result)
