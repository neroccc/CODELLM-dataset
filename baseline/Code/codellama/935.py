from typing import List
class Solution:
    def knightDialer(self, n: int) -> int:
        # Refer to the algorithm description to generate a complete and efficient Python solution for the given Problem Description1

        # Problem Description1
        Given a string `s`, return _the longest_ _palindromic_ _substring_ in `s`.

        **Example 1:**

        **Input:** s =  "babad "
        **Output:**  "bab "
        **Explanation:**  "aba " is also a valid answer.

        **Example 2:**

        **Input:** s =  "cbbd "
        **Output:**  "bb "

        **Constraints:**

        *   `1 <= s.length <= 1000`
        *   `s` consist of only digits and English letters.

        # Python Code
        class Solution:
            def longestPalindrome(self, s: str) -> str:
                n = len(s)
                dp = [[False] * n for _ in range(n)]
                ans = [0, 0]

                for i in range(n):
                    dp[i][i] = True

                for i in range(n - 1):
                    if s[i] == s[i + 1]:
                        dp[i][i + 1] = True
                        ans = [i, i + 1]

                for diff in range(2, n):
                    for i in range(n - diff):
                        j = i + diff
                        if s[i] == s[j] and dp[i + 1][j - 1]:
                            dp[i][j] = True
                            ans = [i, j]

                i, j = ans
                return s[i : j + 1]

        # Refer to the algorithm description to generate a complete and efficient Python solution for the given Problem Description2


        # Problem Description2
        The chess knight has a **unique movement**, it may move two squares vertically and one square horizontally, or two