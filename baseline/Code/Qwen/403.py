from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        dp = {0: {1}}

        for i in range(1, n):
            dp[stones[i]] = set()

        for i in range(n - 1):
            for k in dp[stones[i]]:
                next_stone = stones[i] + k
                if next_stone in dp:
                    dp[next_stone].add(k)
                    if next_stone == stones[-1]:
                        return True
                    if k - 1 > 0:
                        dp[next_stone].add(k - 1)
                    dp[next_stone].add(k + 1)

        return False