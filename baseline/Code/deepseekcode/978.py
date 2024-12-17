from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1] * n
        dp_prev = [1] * n
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                dp[i] = 1
            elif (i-2>=0 and arr[i]>arr[i-1] and arr[i-1]<arr[i-2]) or (i-2>=0 and arr[i]<arr[i-1] and arr[i-1]>arr[i-2]):
                dp[i] = dp_prev[i-1] + 1
            dp_prev[i-1] = dp[i]
        return max(dp)