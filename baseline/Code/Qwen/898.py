from typing import List
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [set() for _ in range(n)]
        dp[0].add(arr[0])
        ans = set(arr)

        for i in range(1, n):
            dp[i].add(arr[i])
            for j in range(i):
                dp[i].add(dp[i - j - 1] | arr[i])
            ans.update(dp[i])

        return len(ans)