from typing import List, Counter


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = [Counter() for _ in range(k)]
        for i in range(n):
            freq[i % k][nums[i]] += 1

        ans = n
        for i in range(k):
            cnt = 0
            for j in range(k):
                cnt += max(freq[j].values()) - freq[j][nums[i + j]]
            ans = min(ans, cnt)

        return ans