import json
import random
import string
from functools import lru_cache
from typing import List


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s1 = word1 + word2
        n = len(s1)
        dp = [[0] * n for i in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            # mark every character as a 1 length palindrome
            dp[i][i] = 1
            for j in range(i + 1, n):
                # new palindrome is found
                if s1[i] == s1[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                    # if the palindrome includes both string consider it as a valid
                    if i < len(word1) and j >= len(word1):
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

        return ans


# Helper function to generate random strings
def generate_random_string(length, charset=string.ascii_lowercase):
    return ''.join(random.choice(charset) for _ in range(length))


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        len_word1 = random.randint(1, 1000)
        len_word2 = random.randint(1, 1000)
        word1 = generate_random_string(len_word1)
        word2 = generate_random_string(len_word2)
        expected_output = solution.longestPalindrome(word1, word2)

        test_cases.append({
            "input": {"word1": word1, "word2": word2},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1771.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
