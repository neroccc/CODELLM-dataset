from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        dp = {}

        def dfs(needs):
            if tuple(needs) in dp:
                return dp[tuple(needs)]

            res = sum(needs[i] * price[i] for i in range(n))

            for offer in special:
                new_needs = [needs[i] - offer[i] for i in range(n)]
                if all(x >= 0 for x in new_needs):
                    res = min(res, dfs(new_needs) + offer[-1])

            dp[tuple(needs)] = res
            return res

        return dfs(needs)