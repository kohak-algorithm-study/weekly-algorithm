class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        reverse_columnTitle = columnTitle[::-1]

        index = 0
        result = 0


        for char_i in reverse_columnTitle:

            if index > 0:
                upper = 26 * index
                result += (ord(char_i) - 64) ** upper
            else:
                result += (ord(char_i)-64)

            index += 26

        return result


columnTitle = "FXSHRXW"
print(Solution().titleToNumber(columnTitle))
