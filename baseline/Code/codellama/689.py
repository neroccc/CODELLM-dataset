from typing import List
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + nums[i]
        
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = presum[i + 1] - presum[i]
        
        for i in range(n - 1):
            dp[i][i + 1] = max(dp[i][i], dp[i + 1][i + 1])
        
        for i in range(n - k):
            for j in range(i + k, n):
                dp[i][j] = max(dp[i][j], dp[i + 1][j], dp[i][j - 1])
        
        i, j, k = 0, k - 1, k * 2
        ans = [0, 0, 0]
        while j < n:
            if dp[i][j] > dp[i][k]:
                ans[2] = k
                k += k - j
                j = k - 1
            else:
                k += k - j
                j = k - 1
            i += 1
        
        return ans