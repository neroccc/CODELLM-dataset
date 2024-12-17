from typing import List
class Solution:
    def longest_subsequence(self, arr: List[int], difference: int) -> int:
        if not arr:
            return 0

        max_depth = 0
        max_length = 1
        dp = {}

        for num in arr:
            if num not in dp:
                dp[num] = 1
            else:
                dp[num] += 1

        for num in arr:
            if num - difference in dp:
                max_depth = max(max_depth, dp[num] + dp[num - difference])
                max_length = max(max_length, dp[num - difference])

        return max_depth