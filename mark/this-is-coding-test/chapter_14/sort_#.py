
class Solution:
    def solution(self, N, stages:list):

        answer = []
        person = len(stages)
        for i in range(1, N+1):
            if i in stages:
                cnt = stages.count(i)
                answer.append(cnt/person)
                person -=  cnt

        return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
Solution().solution(N, stages)