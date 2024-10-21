'''
https://leetcode.com/problems/excel-sheet-column-number/description/
'''


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        columnTitle = columnTitle[::-1]
        for i, char in enumerate(columnTitle):
            result += 26 ** i * (ord(char) - 64)

        return result
