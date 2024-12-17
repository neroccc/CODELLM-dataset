from typing import List
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        dp = [float('inf')] * n
        ans = float('inf')
        left = 0
        total = 0
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            if total == target:
                if left > 0 and dp[left - 1] != float('inf'):
                    ans = min(ans, right - left + 1 + dp[left - 1])
                dp[right] = min(dp[right - 1], right - left + 1)
            else:
                dp[right] = dp[right - 1]
        return -1 if ans == float('inf') else ans