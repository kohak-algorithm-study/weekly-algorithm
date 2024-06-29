def max_food(num_of_warehouses, food_array):

    if not 3 <= num_of_warehouses <= 100:
        return "Number of warehouses should be between 3 and 100."

    if not num_of_warehouses == len(food_array):
        return "Number of warehouses and the length of the food array should be the same."

    get_max = [0] * num_of_warehouses
    get_max[0] = food_array[0]
    get_max[1] = max(food_array[0], food_array[1])

    for i in range(2, num_of_warehouses):
        get_max[i] = max(get_max[i-1], get_max[i-2] + food_array[i])

    return get_max[num_of_warehouses - 1]


input_num_of_warehouses = int(input())
input_food_array = list(map(int, input().split()))

print(max_food(input_num_of_warehouses, input_food_array))
