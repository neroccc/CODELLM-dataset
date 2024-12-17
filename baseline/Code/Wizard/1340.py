from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        max_indices = [0] * n
        min_indices = [n] * n
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] > arr[j]:
                    max_indices[i] = max(max_indices[i], j)
                    min_indices[j] = min(min_indices[j], i)

        count = 0
        for i in range(n):
            if max_indices[i] >= i and i >= min_indices[i]:
                count += 1

        return count