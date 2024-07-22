# 무지의 먹방 라이브 (다시..)
def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    food_times = [(t, i) for i, t in enumerate(food_times, 1)]
    food_times.sort()

    i = 0
    remaining = len(food_times)
    curr = 0
    while k >= 0:

        ncycle = food_times[i][0] - curr
        curr = food_times[i][0]        
        if k == 0:
            tmp = food_times[i:]
            tmp.sort(key=lambda x: x[1])
            return tmp[0][1]
        if k >= remaining * ncycle:
            k -= remaining * ncycle
        else:
            r = k % remaining            
            tmp = food_times[i:]
            tmp.sort(key=lambda x: x[1])
            return tmp[r][1]

        while i < len(food_times) and food_times[i][0] == curr:
            i += 1
            remaining -= 1
