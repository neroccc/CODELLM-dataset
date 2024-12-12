import json
import random

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for len_range in range(2, n + 1):
            for start in range(1, n - len_range + 2):
                end = start + len_range - 1
                dp[start][end] = float("inf")
                for k in range(start, end):
                    dp[start][end] = min(
                        dp[start][end],
                        k + max(dp[start][k - 1], dp[k + 1][end])
                    )
        return dp[1][n]

def generate_test_cases(num_cases=20, max_n=200):
    """
    Generates test cases for the getMoneyAmount function.

    :param num_cases: Number of test cases to generate.
    :param max_n: Maximum value for n.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize n value within the valid range
        n = random.randint(1, max_n)

        # Calculate the expected output using the provided solution
        expected_output = solution.getMoneyAmount(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_375.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=20, max_n=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
