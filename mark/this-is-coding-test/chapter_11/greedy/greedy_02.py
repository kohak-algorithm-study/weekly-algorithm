

n = input()
m = list(n)
int_m = [int(char) for char in m]

int_m.sort()
result = 1

for i in range(len(int_m)):

    if int_m[i] == 0:
        continue
    else:
        result *= int_m[i]

print(result)
