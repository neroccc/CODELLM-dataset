from typing import List
class Solution:
    def num_of_lists(self, num: str) -> int:
        n = len(num)
        dp = [1] * n
        mod = 10**9 + 7

        for i in range(1, n):
            if num[i] != '0':
                dp[i] = 2

        for i in range(1, n):
            for j in range(i):
                if num[i] == '0' and num[j] == '0':
                    continue
                elif int(num[i:j - 1]) <= 9:
                    dp[i] += dp[j - 1]
                    dp[i] %= mod

        return dp[-1] % mod