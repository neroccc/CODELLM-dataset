from typing import List
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        memo = {}

        def dp(i, j, k):
            if (i, j, k) in memo:
                return memo[(i, j, k)]

            if i > j:
                return 0

            if i == j and k == 1:
                return boxes[i] * boxes[i]

            if k == 1:
                memo[(i, j, k)] = dp(i + 1, j, 0) + boxes[i] * boxes[i]
            else:
                memo[(i, j, k)] = dp(i, j - 1, 0)
                for m in range(i, j):
                    if boxes[m] == boxes[j]:
                        memo[(i, j, k)] = max(memo[(i, j, k), dp(i, m, k - 1) + dp(m + 1, j, 0) + boxes[i] * boxes[i]])

            return memo[(i, j, k)]

        return dp(0, len(boxes) - 1, 1)