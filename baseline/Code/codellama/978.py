from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        inc = 1
        dec = 1

        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc += 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec += 1
                inc = 1
            else:
                inc = 1
                dec = 1
            ans = max(ans, inc, dec)
        return ans