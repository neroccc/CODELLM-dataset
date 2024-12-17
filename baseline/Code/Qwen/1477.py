from typing import List
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

        ans = float('inf')
        min_len = [float('inf')] * (n + 1)
        for i in range(n + 1):
            j = i - 1
            while j >= 0 and prefix_sum[i] - prefix_sum[j] > target:
                j -= 1
            if j >= 0:
                min_len[i] = min(min_len[i], i - j)

        for i in range(n, 0, -1):
            j = i + 1
            while j <= n and prefix_sum[j] - prefix_sum[i] > target:
                j += 1
            if j <= n:
                min_len[i] = min(min_len[i], j - i)

        for i in range(n):
            if min_len[i] != float('inf') and min_len[i + min_len[i]] != float('inf'):
                ans = min(ans, min_len[i] + min_len[i + min_len[i]])

        return ans if ans != float('inf') else -1