import math


class Solution:
    def solution(self, progresses, speeds):

        complete_arr = []
        answer = []

        for i in range(len(progresses)):

            complete = math.ceil((100 - progresses[i]) / speeds[i])
            complete_arr.append(complete)

        cnt = 1
        for j in range(len(complete_arr) - 1):
            if complete_arr[j] >= complete_arr[j + 1]:
                cnt += 1
            else:
                answer.append(cnt)
                cnt = 1

        answer.append(cnt)

        return answer


progresses = [20, 99, 93, 30, 55]
speeds =[5, 1, 30, 30, 5]
print(Solution().solution(progresses, speeds))