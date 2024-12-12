import json
import random
import string
from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        M: int = len(s)
        N: int = len(t)

        # Dynamic Programming table
        dp: List[List[int]] = [[0 for _ in range(N + 1)] for _ in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]

def generate_test_cases(num_cases=1000, max_length=100):
    """
    Generates test cases for the numDistinct function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the strings.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize lengths for s and t
        len_s = random.randint(1, max_length)
        len_t = random.randint(1, min(len_s, max_length))

        # Generate random strings
        s = ''.join(random.choices(string.ascii_lowercase, k=len_s))
        t = ''.join(random.choices(string.ascii_lowercase, k=len_t))

        # Calculate the expected output using the provided solution
        expected_output = solution.numDistinct(s, t)

        # Add test case
        test_cases.append({
            "input": {"s": s, "t": t},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_115.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=1000, max_length=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
