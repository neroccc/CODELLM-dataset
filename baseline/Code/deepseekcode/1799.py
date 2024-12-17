from typing import List
from deepseekcode.help.helphelp import gcd


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums.sort()
        dp = [0] * (1 << (2 * n))
        g = [[0] * (n * 2) for _ in range(n * 2)]
        cnt = [0] * (1 << (2 * n))
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g[i][j] = g[j][i] = gcd(nums[i], nums[j])
        for i in range(1 << (2 * n)):
            cnt[i] = cnt[i & (i - 1)] + ((i & 1) == 1)
        for i in range(1, 1 << (2 * n)):
            if cnt[i] % 2 == 1:
                continue
            t = [j for j in range(2 * n) if ((i >> j) & 1) == 1]
            if len(t) < 2:
                continue
            dp[i] = max(dp[i ^ (1 << j)] + cnt[i] // 2 * g[t[0]][t[1]])
        return dp[(1 << (2 * n)) - 1]