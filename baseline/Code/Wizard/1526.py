from typing import List
class Solution:
    def minOperations(self, target: List[int], initial: List[int]) -> int:
        n = len(target)
        ans = 0
        for i in range(n):
            if target[i] != initial[i]:
                ans += abs(target[i] - initial[i])
        return ans