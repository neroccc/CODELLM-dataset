from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        visited = [False] * n
        max_jumps = 0
        for i in range(n):
            if visited[i]:
                continue
            max_jumps += 1
            visited[i] = True
            for j in range(i - 1, -1, -1):
                if visited[j]:
                    continue
                if arr[j] < arr[i]:
                    visited[j] = True
                    break
            for j in range(i + 1, n):
                if visited[j]:
                    continue
                if arr[j] < arr[i]:
                    visited[j] = True
                    break
        return max_jumps