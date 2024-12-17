from typing import List
class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * target
        for i in range(1, target + 1):
            for j in range(9):
                if i >= cost[j]:
                    dp[i] = max(dp[i], dp[i - cost[j]] + 1)
        if dp[target] == -1:
            return "0"
        ans = []
        for i in range(9, -1, -1):
            while dp[target] > 0 and dp[target] == dp[target - cost[i]] + 1:
                ans.append(str(i + 1))
                target -= cost[i]
                dp[target] -= 1
        return "".join(ans)