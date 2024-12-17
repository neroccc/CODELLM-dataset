from typing import List
class Solution:
    def longestSubarray(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = arr[i]

        for i in range(n - 1):
            if arr[i] == arr[i + 1]:
                dp[i][i + 1] = arr[i]
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if arr[i] == arr[j] and dp[i + 1][j - 1]:
                    dp[i][j] = arr[i]
                    ans = [i, j]

        i, j = ans
        return sum(arr[i : j + 1])