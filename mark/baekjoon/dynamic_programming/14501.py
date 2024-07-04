
n = int(input().strip())
arr =  []

value = []

for _ in range(n):
    t, p = map(int, input().strip().split())
    arr.append((t, p))

for index, arr1 in enumerate(arr):

    if arr1[0] + (index + 1) <= len(arr):
        value.append((arr1[0], arr1[1] ,int(arr1[1]/arr1[0])))

value.sort(key=lambda x: x[2], reverse=True)

print(value)

result = 0
day = 0

for value1 in value:

    day += value1[0]

    if day > n:
        break
    result += value1[1]


print(result)




