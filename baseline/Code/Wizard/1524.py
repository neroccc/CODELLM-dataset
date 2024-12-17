from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        presum = [0] * (n + 1)
        for i in range(n):
            presum[i + 1] = presum[i] + arr[i]

        count = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (presum[j] - presum[i]) % 2 != 0:
                    count += j - i

        return count % mod