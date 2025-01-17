
class Solution:
    def solution(self, nums):


        aa = len(nums) / 2
        set_nums = set(nums)

        if aa > len(set_nums):
            answer = len(set_nums)
        else:
            answer = aa
        return answer


nums = [3,1,2,3]
print(Solution().solution(nums))