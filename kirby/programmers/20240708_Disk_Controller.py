# https://school.programmers.co.kr/learn/courses/30/lessons/42627

import heapq


def solution(jobs: list) -> int:
    jobs.sort()

    time = 0
    total_wait_time = 0
    completed_count = 0
    job_index = 0

    heap_q = []
    while completed_count < len(jobs):
        # 현재 시점에서 실행 가능한 작업을 힙에 추가
        while job_index < len(jobs) and jobs[job_index][0] <= time:
            heapq.heappush(heap_q, (jobs[job_index][1], jobs[job_index][0]))  # 작업 시간, 요청 시간
            job_index += 1

        # 최소 대기 작업을 선택
        if heap_q:
            current_job = heapq.heappop(heap_q)
            time += current_job[0]  # 작업 시간을 더한다.
            total_wait_time += (time - current_job[1])  # 대기 시간을 더한다.
            completed_count += 1  # 완료된 작업 수를 더한다.
        # 힙이 비어있다면 다음 작업의 요청 시간으로 이동
        else:
            time = jobs[job_index][0]

    return total_wait_time // len(jobs)


# 테스트 예제
print(solution([[0, 3], [1, 9], [2, 6]]))  # 9
