from typing import List
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        import collections
        import math
        import heapq

        n = len(nums)
        dp = [0] + [-math.inf] * 2**k
        for i in range(k):
            cnt = collections.Counter(nums[i::k])
            nxt = [0] + [-math.inf] * 2**k
            for x in range(2**k):
                for y, v in cnt.items():
                    nxt[x] = max(nxt[x], dp[x^y] + v)
            dp = nxt
        return n - max(dp[x^(2**k-1)] for x in range(2**k))