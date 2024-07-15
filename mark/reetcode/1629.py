from typing import List


class Solution:
    def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:

        duration = []
        print(len(releaseTimes))
        for i in range(len(releaseTimes)):

            if i == 0:
                duration.append((keysPressed[i], releaseTimes[i]))
            else:
                duration.append(((keysPressed[i], releaseTimes[i] - releaseTimes[i - 1])))

        sorted_data = sorted(duration, key=lambda x: (x[1],x[0]) ,reverse=True)
        return sorted_data[0][0]

releaseTimes = [9, 29, 49, 50]
keysPressed = "cbcd"
print(Solution.slowestKey(releaseTimes, keysPressed))

'''
https://leetcode.com/problems/slowest-key/description/
'''