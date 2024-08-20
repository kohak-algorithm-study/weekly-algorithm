'''
https://school.programmers.co.kr/learn/courses/30/lessons/17681
'''


def convert_to_binary_num_map(n, decimal_num_array):
    array = []
    for decimal_num in decimal_num_array:
        bin_num = bin(decimal_num)[2:].zfill(n)
        array.append(list(map(int, bin_num)))
    return array


def solution(n, arr1, arr2):
    answer = []
    map1 = convert_to_binary_num_map(n, arr1)
    map2 = convert_to_binary_num_map(n, arr2)
    for i in range(n):
        row = ''
        for j in range(n):
            if map1[i][j] == 0 and map2[i][j] == 0:
                row += ' '
            else:
                row += '#'
        answer.append(row)
    return answer


def solution2(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        arr12 = bin(i | j)[2:]  # |는 비트 OR 연산
        arr12 = arr12.zfill(n)

        arr12 = arr12.replace('1', '#')
        arr12 = arr12.replace('0', ' ')
        answer.append(arr12)
    return answer


# result = solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
result = solution2(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
print(result)
