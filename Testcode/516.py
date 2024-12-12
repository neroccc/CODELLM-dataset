import json
import random
from typing import List


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Base case: a single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        # Iterate over substrings of length 2 to n
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate a random string of length between 1 and 1000
        string_length = random.randint(1, 100)
        s = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=string_length))

        # Calculate the expected output using the solution
        expected_output = solution.longestPalindromeSubseq(s)

        # Add test case
        test_cases.append({
            "input": {"s": s},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_516.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
