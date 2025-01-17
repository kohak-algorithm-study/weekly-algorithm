import math


class Solution:
    def solution(self, priorities, location):

        alphabet = [chr(c) for c in range(97, 97+len(priorities))]
        process_queue = list()

        for i,alpha in enumerate(alphabet):
            process_queue.append((alpha, priorities[i]))

        answer = 0

        return answer


priorities = [2, 1, 3, 2]
location = 2
print(Solution().solution(priorities, location))