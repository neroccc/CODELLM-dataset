from typing import List
class Solution:
    def count_ways(self, nums: List[int]) -> int:
        def count_unique_trees(n: int) -> int:
            MOD = 10**9 + 7
            dp = [1] * (n + 1)
            for i in range(2, n + 1):
                for j in range(1, i):
                    dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % MOD
            return dp[n]

        def count_unique_bst(n: int) -> int:
            MOD = 10**9 + 7
            dp = [1] * (n + 1)
            for i in range(2, n + 1):
                for j in range(1, i):
                    dp[i] = (dp[i] + dp[j] * dp[i - j - 1]) % MOD
            return dp[n]

        def count_unique_bst_with_range(n: int, start: int, end: int) -> int:
            MOD = 10**9 + 7
            if start > end:
                return 1
            if start == end:
                return 1
            count = 0
            for i in range(start, end + 1):
                count += count_unique_bst(i - 1) * count_unique_bst_with_range(n - i, i + 1, end)
                count %= MOD
            return count

        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n):
            count += count_unique_bst_with_range(i, 1, n - 1) * count_unique_trees(n - i - 1)
            count %= 10**9 + 7
        return count