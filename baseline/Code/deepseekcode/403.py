from typing import List
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_positions = set(stones)
        dp = [set() for _ in range(len(stones))]
        dp[0].add(0)

        for i in range(1, len(stones)):
            for j in range(i):
                diff = stones[i] - stones[j]
                if diff-1 in dp[j] or diff in dp[j] or (diff+1 in dp[j] and diff+1>0):
                    dp[i].add(diff)
                    if i == len(stones) - 1:
                        return True
        return False