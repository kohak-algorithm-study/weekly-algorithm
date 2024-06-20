
n = int(input())
parts = list(map(int, input().split()))

m = int(input())
find_part = list(map(int, input().split()))

for i in find_part:

    if i in parts:
        print("yes", end=" ")
    else:
        print("no", end=" ")
