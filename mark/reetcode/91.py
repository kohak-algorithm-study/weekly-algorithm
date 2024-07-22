class Solution:
    def numDecodings(self, s: str) -> int:

        s_one_split_list = []
        s_two_split_list = []
        s_tow_split_list_back = []

        if len(s) >= 2:
            s_one_split_list = self.split_by_one(s)
            s_two_split_list = self.split_by_two(s)

        if len(s) % 2 == 1:
            s_tow_split_list_back = self.split_by_two_reverse(s)

        aList = [str(i) for i in range(1,27)]

        cnt = 0

        if len(s_one_split_list) != 0:
            if all(s_one in aList for s_one in s_one_split_list):
                cnt += 1
        if len(s_two_split_list) != 0:
            if all(s_two in aList for s_two in s_two_split_list):
                cnt += 1

        if len(s_tow_split_list_back) != 0:
            if all(s_two_reverse in aList for s_two_reverse in s_tow_split_list_back):
                cnt += 1

        return cnt


    def split_by_one(self, s):
        return [s[i:i + 1] for i in range(0, len(s), 1)]
    def split_by_two(self, s):
        return [s[i:i + 2] for i in range(0, len(s), 2)]

    def split_by_two_reverse(self, s):
        reversed_s = s[::-1]
        split_reversed = [reversed_s[i:i + 2] for i in range(0, len(reversed_s), 2)]
        result = [chunk[::-1] for chunk in split_reversed]
        return result[::-1]


print(Solution().numDecodings("2106"))