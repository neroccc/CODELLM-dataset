import json
import random
import string
from typing import List

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        # find the LCS of s1 and s2
        lcs = self.getLCS(s1, s2)
        i, j = 0, 0
        result = ""
        # merge s1 and s2 with the LCS
        for c in lcs:
            # add characters from s1 until the LCS character is found
            while s1[i] != c:
                result += s1[i]
                i += 1
            # add characters from s2 until the LCS character is found
            while s2[j] != c:
                result += s2[j]
                j += 1
            # add the LCS character
            result += c
            i += 1
            j += 1
        # add any remaining characters from s1 and s2
        result += s1[i:] + s2[j:]
        # return the merged string
        return result

    # helper method to find the LCS of two strings
    def getLCS(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        # fill the dp array using dynamic programming
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # backtrack from the bottom right corner of the dp array to find the LCS
        lcs = ""
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                lcs = s1[i-1] + lcs
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        return lcs


def generate_random_string(min_length=1, max_length=1000):
    """Generate a random string of lowercase English letters."""
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def generate_test_cases(num_cases=50, max_length=1000):
    """Generate test cases for the Shortest Common Supersequence problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        s1 = generate_random_string(1, max_length)
        s2 = generate_random_string(1, max_length)
        expected_output = solution.shortestCommonSupersequence(s1, s2)
        test_cases.append({
            "input": {"s1": s1, "s2": s2},
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"s1": "abac", "s2": "cab"},
         "output": solution.shortestCommonSupersequence("abac", "cab")},
        {"input": {"s1": "aaaaaaaa", "s2": "aaaaaaaa"},
         "output": solution.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa")},
        {"input": {"s1": "abc", "s2": "def"},
         "output": solution.shortestCommonSupersequence("abc", "def")},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_length = 1000
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("../test_cases_1092.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'shortest_common_supersequence_test_cases.json'.")
