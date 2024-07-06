# https://leetcode.com/problems/count-collisions-on-a-road/description/
# Difficulty: Medium

from collections import defaultdict


class Solution:
    def countCollisions(self, directions: str) -> int:
        collisions_count = 0
        road = defaultdict(int)

        for direction in directions:
            if direction == 'L':
                if road['R'] > 0:
                    collisions_count += 2
                    collisions_count += (road['R'] - 1)
                    road['R'] = 0
                    road['S'] += 1
                elif road['S'] > 0:
                    collisions_count += 1
            if direction == 'R':
                road['R'] += 1
            if direction == 'S':
                collisions_count += road['R']
                road['R'] = 0
                road['S'] += 1

            # print('direction', direction)
            # print('road', road)
            # print('collisions_count', collisions_count)

        return collisions_count


print(Solution().countCollisions("RLRSLL"))  # 5
print(Solution().countCollisions("LLRR"))  # 0
