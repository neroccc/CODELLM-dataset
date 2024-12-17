from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        arr = [0] + arr + [0]
        res = 0
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                left = stack[-1]
                right = i
                res += arr[j] * (j - left) * (right - j)
                res %= MOD
            stack.append(i)
        return res