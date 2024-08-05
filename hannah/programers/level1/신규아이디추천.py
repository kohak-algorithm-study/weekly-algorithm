'''
https://school.programmers.co.kr/learn/courses/30/lessons/72410
'''
import re


def change_lower(new_id):
    return new_id.lower()


def replace_not_allowed(new_id):
    allowed = ['-', '_', '.']
    copy_new_id = new_id
    for x in copy_new_id:
        if x.isalpha() or x.isdigit() or x in allowed:
            continue
        new_id = new_id.replace(x, '')

    return new_id


def replace_double_dots(new_id):
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    return new_id


def remove_first_last_dot(new_id):
    return new_id.strip('.')


def check_empty(new_id):
    if new_id == '':
        return 'a'
    return new_id


def check_max_length(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    return remove_first_last_dot(new_id)


def check_min_length(new_id):
    if len(new_id) <= 2:
        last_word = new_id[-1]
        while len(new_id) < 3:
            new_id += last_word
    return new_id


def solution(new_id):

    new_id = change_lower(new_id)
    new_id = replace_not_allowed(new_id)
    new_id = replace_double_dots(new_id)
    new_id = remove_first_last_dot(new_id)
    new_id = check_empty(new_id)
    new_id = check_max_length(new_id)
    new_id = check_min_length(new_id)

    return new_id


# result = solution("z-+.^.")  # "z--"
# result = solution("=.=")  # "aaa"
result = solution("...!@BaT#*..y.abcdefghijklm")  # "bat.y.abcdefghi"

print()
print()
print()
print(f'result: {result}')


def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for _ in range(3 - len(st))])
    return st
