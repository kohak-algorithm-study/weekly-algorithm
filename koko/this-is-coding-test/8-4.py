def all_ways_of_tile_construction(width):

    if not 1 <= width <= 100:
        return "Input number should be between 1 and 100."

    num_of_ways = [0] * (width+1)

    num_of_ways[1] = 1
    num_of_ways[2] = 3

    for i in range(3, width + 1):
        num_of_ways[i] = (num_of_ways[i - 1] + 2 * num_of_ways[i - 2]) % 796796

    return num_of_ways[width]


input_width = int(input())
print(all_ways_of_tile_construction(input_width))
