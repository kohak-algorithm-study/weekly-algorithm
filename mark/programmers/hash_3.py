class Solution:
    def solution(self, participant, completion):

        for i in completion:
            participant.remove(i)

        print(participant)
        answer = participant[0]

        return answer
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

Solution().solution(participant, completion)

