import numbers

s = input()

alphabet_list = []
number = 0

for char_s in s:

    if char_s.isdecimal():
        number += int(char_s)
    else:
        alphabet_list.append(char_s)

result = ''.join(sorted(alphabet_list)) + str(number)
print(result)



# K1KA5CB7
# AJKDLSI412K4JSJ9D