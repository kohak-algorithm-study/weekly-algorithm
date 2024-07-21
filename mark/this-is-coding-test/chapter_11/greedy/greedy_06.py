
def solution(food_times, k):

    food = 0


    for i in range(k):
        for j in range( len(food_times)):

            if food_times[food] == 0:
                food += 1
            else:
                food_times[food] = food_times[food] - 1
                food += 1

            if food == len(food_times):
                food = 0

    answer = food + 1

    return answer


result = solution([3 ,1 ,2], 5)
print(result)
