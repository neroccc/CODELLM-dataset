from typing import List
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if n == 1:
            return 0 if stones[0] == k else -1
        if n % (k - 1) != 0:
            return -1

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if length % k == 0:
                    dp[i][j] = float('inf')
                    for m in range(i, j, k):
                        dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
                elif length % k != 0:
                    dp[i][j] = float('inf')
                    for m in range(i, j - k + 1, k):
                        dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + k][j])

        for i in range(n):
            for j in range(i + 1, n):
                dp[i][j] += sum(stones[i:j + 1])

        return dp[0][n - 1] if dp[0][n - 1] != float('inf') else -1