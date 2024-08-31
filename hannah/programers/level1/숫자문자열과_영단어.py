'''
https://school.programmers.co.kr/learn/courses/30/lessons/81301
'''

number_dict = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def solution(s):
    result = ''
    start = 0
    end = 0
    while start < len(s) and end <= len(s):
        if s[start].isdigit():
            result += s[start]
            start += 1
            continue

        end = start + 3  # 영어가 최소 3글자이므로
        while end <= len(s):
            if s[start:end] in number_dict:
                result += number_dict[s[start:end]]
                start = end
                break
            else:
                end += 1

    return int(result)


def solution2(s):
    for k, v in number_dict.items():
        s = s.replace(k, v)
    return int(s)


result = solution2("one4seveneight")
print(result)
