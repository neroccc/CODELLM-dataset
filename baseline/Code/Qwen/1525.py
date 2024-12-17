from typing import List
class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left = [0] * n
        right = [0] * n
        left_set = set()
        right_set = set(s[n - 1])

        for i in range(n):
            left_set.add(s[i])
            right_set.add(s[n - 1 - i])
            left[i] = len(left_set)
            right[n - 1 - i] = len(right_set)

        ans = 0
        for i in range(n - 1):
            if left[i] == right[i + 1]:
                ans += 1

        return ans