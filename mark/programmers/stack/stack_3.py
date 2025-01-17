import math


class Solution:
    def solution(self, s):

        stack = []

        for i,s_char in enumerate(s):

            if s_char == "(":
                stack.append("(")
            else:
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()

        if len(stack) > 0:
            return False

        return True


s = "(())((()())("
print(Solution().solution(s))