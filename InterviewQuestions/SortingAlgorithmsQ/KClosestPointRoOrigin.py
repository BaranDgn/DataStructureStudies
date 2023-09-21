# K Closest Point to Origin

"""
Given an array of 'points' where 'points[i] = [xi, yi]' represents a point
on X-Y plane and an integer 'k', return the 'k' closest points to origin (0,0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e. [(x1-x2)^2 + (y1-y2)^2]^2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example1:
Input: points = [[1,3], [-2,2]] , k = 1
Output : [[-2,2]]

"""
from typing import List
import math
import heapq


class Solution:
    def kClosestPoint(self, points: List[int], k):
        minHeap = []

        for x, y in points:
            distanceToOrigin = (x ** 2) + (y ** 2)
            minHeap.append([distanceToOrigin, x, y])

        heapq.heapify(minHeap)  # min heap python kutuphanesi sayesinde min heap e dönüştürür.

        result = []

        while k > 0:
            distance, x, y = heapq.heappop(minHeap)  # heap ten eleman cıkamak icin, bu sekilde bana bir tane distanceToOrigin, x ve y verecek. Bu saye istenen en küçük değer alınabilir.
            result.append([x, y])
            k -= 1

        return result


sol = Solution()
print(sol.kClosestPoint([[1, 3], [-2, 2]], 1))
print(sol.kClosestPoint([[3, 3], [5, -1], [-2, 4]], 2))
