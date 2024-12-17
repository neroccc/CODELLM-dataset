from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10**9 + 7
        stack = []
        ans = dot = 0
        for i, a in enumerate(arr + [float('inf')]):
            while stack and arr[stack[-1]][0] > a:
                _, x, m = stack.pop()
                dot -= x * (i - stack[-1][1]) * (i - x)
                dot %= mod
            if not stack or arr[stack[-1][0]] != a:
                stack.append((i, i, a))
            else:
                stack[-1] = (i, stack[-1][1], min(stack[-1][2], a))
            dot += a * (i - stack[-1][1]) * (i - stack[-1][0])
            dot %= mod
        return dot % mod