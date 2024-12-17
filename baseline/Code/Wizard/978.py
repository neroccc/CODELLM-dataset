from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1

        ans = 1
        count = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                if i == n - 1 or (arr[i] > arr[i + 1]):
                    count += 1
                else:
                    ans = max(ans, count)
                    count = 1
            elif arr[i] < arr[i - 1]:
                if i == n - 1 or (arr[i] < arr[i + 1]):
                    count += 1
                else:
                    ans = max(ans, count)
                    count = 1
            else:
                ans = max(ans, count)
                count = 1

        return max(ans, count)