from typing import List
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return n

        freq = [0] * 210
        for num in nums:
            freq[num] += 1

        xor = 0
        for i in range(210):
            if freq[i] % 2 != 0:
                xor ^= i

        if xor == 0:
            return 0

        for i in range(210):
            if freq[i] % 2 != 0:
                freq[i] -= 1

        for i in range(n):
            if i % k == 0:
                xor = 0
            xor ^= nums[i]
            if i >= k - 1:
                if xor == 0:
                    continue
                for j in range(210):
                    if freq[j] % 2 != 0:
                        freq[j] -= 1
                        xor ^= j
                if i + 1 == k:
                    return k - freq[xor].bit_length() // 2

        return -1