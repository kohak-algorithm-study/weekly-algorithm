'''
https://school.programmers.co.kr/learn/courses/30/lessons/60058
'''


def solution(p):
    result = ''
    if p == '':
        return result

    u, v = make_u_v(p)
    if check_completed(u):
        result += u
        result += solution(v)
    else:
        # 4번 과정 진행
        result = '('
        result += solution(v)
        result += ')'

        u = list(u)[1:-1]
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        result += ''.join(u)

    return result


def check_completed(u):
    open_b = []
    for x in u:
        if x == '(':
            open_b.append(x)
        else:
            if open_b and open_b[-1] == '(':
                open_b.pop()
            else:
                open_b.append(x)
    if open_b:
        return False

    return True


def make_u_v(p):
    open_b_count = 0
    for i in range(len(p)):
        if p[i] == '(':
            open_b_count += 1
        else:
            open_b_count -= 1

        if open_b_count == 0:
            return p[:(i + 1)], p[(i + 1):]
    else:  # TODO: 균형 문자열이 없다면????
        return p, ''


result = solution(")(")
print(result)
