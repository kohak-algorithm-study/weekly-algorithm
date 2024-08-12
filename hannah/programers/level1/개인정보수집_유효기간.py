'''
https://school.programmers.co.kr/learn/courses/30/lessons/150370
'''

from datetime import datetime


def solution(today, terms, privacies):
    answer = []
    terms_expired_info = {x.split()[0]: int(x.split()[1]) for x in terms}
    today = today.replace('.', '')

    for idx, privacy in enumerate(privacies):

        in_date, terms_code = privacy.split()
        print(f'in date: {in_date}')
        print(f'expired: {terms_expired_info[terms_code]}')

        in_date_year = int(in_date.split('.')[0])
        in_date_month = int(in_date.split('.')[1])
        in_date_day = int(in_date.split('.')[2])

        expired_date_date = in_date_day - 1
        expired_date_month = in_date_month + terms_expired_info[terms_code]
        expired_date_year = in_date_year

        if expired_date_date < 1:
            expired_date_date = 28
            expired_date_month -= 1

        if expired_date_month > 12:
            print("=====12월 지남====")
            expired_date_year += expired_date_month // 12
            expired_date_month = expired_date_month % 12

        if expired_date_month == 0:
            expired_date_month = 12
            expired_date_year -= 1
        print(f'expired_date_y: {expired_date_year}')
        print(f'expired_date_m: {expired_date_month}')
        print(f'expired_date_date: {expired_date_date}')

        expired_date = datetime(expired_date_year, expired_date_month, expired_date_date)
        print(f'result= {expired_date.strftime("%Y%m%d")}')
        if expired_date.strftime('%Y%m%d') < today:
            answer.append(idx + 1)
        print()
    return answer


result = solution("2020.12.28", ["A 1"], ["2020.12.28 A"])
print(result)
# 기댓값: []


def solution2(today, terms, privacies):

    def _convert_date_by_int(date_by_string):
        y, m, d = map(int, date_by_string.split('.'))
        return (y * 12 * 28) + (m * 28) + d

    answer = []

    terms_expired_info = {x.split()[0]: int(x.split()[1]) for x in terms}
    today_by_int = _convert_date_by_int(today)

    for idx, privacy in enumerate(privacies):
        in_date, terms_code = privacy.split()
        in_date_by_int = _convert_date_by_int(in_date)
        expire_date_by_int = in_date_by_int + terms_expired_info[terms_code] * 28 - 1

        if expire_date_by_int < today_by_int:
            answer.append(idx + 1)

    return answer
