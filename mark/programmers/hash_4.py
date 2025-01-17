class Solution:
    def solution(self, clothes):

        c_map = {}

        for clothe in clothes:
            if clothe[1] in c_map:
                c_map[clothe[1]] += 1
            else:
                c_map[clothe[1]] = 1

        answer = 1

        for count in c_map.values():
            answer *= (count + 1)

        return ''
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

Solution().solution(clothes)

