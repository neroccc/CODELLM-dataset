from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort(reverse=True)
        ans = 0
        sum = 0
        for i in range(n):
            sum += satisfaction[i]
            ans += i * sum
        return ans