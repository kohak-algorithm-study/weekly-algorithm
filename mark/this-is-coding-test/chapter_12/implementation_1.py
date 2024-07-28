


n = input()

left_cnt = 0
right_cnt = 0

for i in range(len(n)):

    if i < len(n)/2:
        left_cnt += int(n[i])
    else:
        right_cnt += int(n[i])

if left_cnt == right_cnt:
    print('LUCKY')
else:
    print('READY')

