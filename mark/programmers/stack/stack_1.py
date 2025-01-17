
class Solution:
    def solution(self, arr):

        temp = None
        answer = []

        for a in arr:
            if temp != a:
                answer.append(a)
                temp = a
            else:
                continue

        return answer

arr = [1,1,3,3,0,1,1]
print(Solution().solution(arr))