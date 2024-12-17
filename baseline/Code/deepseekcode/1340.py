from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        indices = sorted(range(n), key=lambda i: arr[i])
        dp = [1] * n

        for index in indices:
            for dx in range(-1, 2, 2):
                for x in range(1, d + 1):
                    nx = index + dx * x
                    if nx < 0 or nx >= n or abs(arr[nx] - arr[index]) > x:
                        break
                    if arr[nx] < arr[index]:
                        dp[index] = max(dp[index], dp[nx] + 1)

        return max(dp)