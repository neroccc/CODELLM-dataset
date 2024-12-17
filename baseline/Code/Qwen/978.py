from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * 2 for _ in range(n)]
        ans = 1

        for i in range(n):
            if i == 0:
                dp[i][0] = 1
                dp[i][1] = 1
            else:
                if arr[i] > arr[i - 1]:
                    dp[i][0] = dp[i - 1][1] + 1
                    dp[i][1] = 1
                elif arr[i] < arr[i - 1]:
                    dp[i][0] = 1
                    dp[i][1] = dp[i - 1][0] + 1
                else:
                    dp[i][0] = 1
                    dp[i][1] = 1

            ans = max(ans, dp[i][0], dp[i][1])

        return ans