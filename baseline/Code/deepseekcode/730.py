from typing import List
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mod = 10**9 + 7
        alphabet_size = 4
        str_length = len(s)
        char_to_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

        dp = [[[0]*alphabet_size for _ in range(str_length)] for _ in range(str_length)]
        for i in range(str_length):
            dp[i][i][char_to_index[s[i]]] = 1

        for length in range(2, str_length+1):
            for i in range(str_length-length+1):
                j = i+length-1
                for k in range(alphabet_size):
                    for x in range(alphabet_size):
                        if k == x:
                            dp[i][j][k] = dp[i+1][j-1][x]*2
                        else:
                            dp[i][j][k] = dp[i+1][j-1][x]
                        dp[i][j][k] %= mod

                for x in range(alphabet_size):
                    dp[i][j][char_to_index[s[i]]] += dp[i+1][j][x]
                    dp[i][j][char_to_index[s[i]]] %= mod
                for x in range(alphabet_size):
                    dp[i][j][char_to_index[s[j]]] += dp[i][j-1][x]
                    dp[i][j][char_to_index[s[j]]] %= mod

        return sum(dp[0][str_length-1]) % mod