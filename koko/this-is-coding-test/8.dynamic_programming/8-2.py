def min_operations_to_make_one(num):
    counts = [0] * (num+1)

    if num > 30000:
        return "Input number is too large."

    for i in range(2, num+1):
        counts[i] = counts[i-1] + 1
        if i % 2 == 0:
            counts[i] = min(counts[i], counts[i//2] + 1)
        if i % 3 == 0:
            counts[i] = min(counts[i], counts[i//3] + 1)

    return counts[num]


input_number = int(input())
print(min_operations_to_make_one(input_number))
