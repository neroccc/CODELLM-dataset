from typing import List
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [1] * n
        indices = list(range(n))
        indices.sort(key=lambda i: arr[i], reverse=True)

        for i in indices:
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    break

            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                else:
                    break

        return max(dp)