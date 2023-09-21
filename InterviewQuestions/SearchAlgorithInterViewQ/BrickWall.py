# Brick Wall - GOOGLE *****

"""
There is a rectangular brick in front of you with 'n' rows of bricks.
The i^th row has some number of bricks each of the same height(i.e. one unit)
but they can be of different widths. The total width of each row is the same.

Draw a vertical line from top to bottom and cross the least bricks. If your line goes through the edge of brick,
then the brick is not considered as crossed. You cannot draw a line just along one of the two vertical edges of the wall,
in which case the line will obviously cross no bricks.

Given the 2D array 'wall' that contains the information about the wall, return the minimum number of crossed bricks
after drawing such a vertical line.

Input: wall = [[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]
Output: 2

Input = wall = [[1],[1],[1]]
Output : 3 // Hiç boşluk olmayacagı icin hepsi kırılacak.

"""
from typing import List


class Solution:
    def leastBrick(self, wall: List[int]) -> int:
        gap = {0: 0}

        for row in wall:
            gapIndex = 0
            for brick in row[:-1]: # En son elemana bakmaya gerek yoktur. Cunku edge kısımlarındaki boslukları almıyoruz.
                gapIndex += brick
                gap[gapIndex] = 1 + gap.get(gapIndex, 0) # Daha önce den bu indekste deger yoksa, hata vermesin diye böyle yaptık.
        maxGapNumber = max(gap.values())
        rowNumber = len(wall)
        return rowNumber - maxGapNumber







sol = Solution()
print(sol.leastBrick([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]))
print(sol.leastBrick([[1],[1],[1]]))

