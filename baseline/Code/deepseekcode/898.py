from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        dp = [set() for _ in range(len(arr))]
        for i, num in enumerate(arr):
            dp[i].add(num)
            if i > 0:
                for num2 in dp[i-1]:
                    dp[i].add(num2 | num)
            res.update(dp[i])
        return len(res)