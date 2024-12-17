from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def helper(needs):
            key = tuple(needs)
            if key in memo:
                return memo[key]
            cost = sum(needs[i] * price[i] for i in range(len(needs)))
            for offer in special:
                if all(needs[i] >= offer[i] for i in range(len(needs))):
                    remaining = [needs[i] - offer[i] for i in range(len(needs))]
                    cost = min(cost, helper(remaining) + offer[-1])
            memo[key] = cost
            return cost

        memo = {}
        return helper(needs)