from typing import List
class Solution:
    def oddSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            dp[i][i] = 1
            ans += 1

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if arr[i] + arr[j] % 2 == 1:
                    dp[i][j] = dp[i + 1][j - 1] + 1
                    ans += dp[i][j]

        return ans % (10 ** 9 + 7)