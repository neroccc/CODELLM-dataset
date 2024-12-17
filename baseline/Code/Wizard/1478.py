from typing import List
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        n = len(houses)
        if k > n:
            return 0

        def dist(i, j):
            return houses[j] - houses[i]

        def min_dist(i, j, k):
            if k == 1:
                return dist(i, j)
            if k == 2:
                return min(dist(i, j), dist(i, j - 1))

            if k > n - i:
                return min_dist(i, j, n - i)

            mid = (i + j) // 2
            return min(min_dist(i, mid, k // 2) + min_dist(mid + 1, j, (k + 1) // 2), min_dist(i, j, k - 1) + dist(mid, j))

        return min_dist(0, n - 1, k)