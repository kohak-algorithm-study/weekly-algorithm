'''
https://school.programmers.co.kr/learn/courses/30/lessons/92334
'''


def solution(id_list, report, k):
    reportee_cnts = [0] * len(id_list)
    for x in set(report):
        idx = id_list.index(x.split()[1])
        reportee_cnts[idx] += 1

    result = [0] * len(id_list)
    for x in set(report):
        reporter_idx = id_list.index(x.split()[0])
        reportee_idx = id_list.index(x.split()[1])
        if reportee_cnts[reportee_idx] >= k:
            result[reporter_idx] += 1

    return result


def _solution(id_list, reports, k):
    name_idx_dict = {name: idx for idx, name in enumerate(id_list)}
    n = len(id_list)
    report_map = [[0] * n for _ in range(n)]

    for report in reports:
        reporter, reportee = report.split()

        if report_map[name_idx_dict[reporter]][name_idx_dict[reportee]] == 0:
            report_map[name_idx_dict[reporter]][name_idx_dict[reportee]] = 1

    report_cnt = [0] * n
    for i in range(n):
        report_cnt[i] = sum(x[i] for x in report_map)

    result_reportee_idx = [i for i, cnt in enumerate(report_cnt) if cnt >= k]

    # 신고한 사람 찾기
    result = [0] * n
    for i in range(n):
        for j in range(n):
            if j in result_reportee_idx and report_map[i][j] == 1:
                result[i] += 1
    return result
