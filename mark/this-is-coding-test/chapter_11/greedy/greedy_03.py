


s = input()
s_list = list(s)

cnt_0 = 0
cnt_1 = 0

tempt = ''

for i in range(len(s_list)):

    if tempt != s_list[i]:

       if s_list[i] == '0':
            cnt_0 += 1
       elif s_list[i] == '1':
           cnt_1 += 1

       tempt = s_list[i]

    else:
        continue

print(min(cnt_0,cnt_1))

