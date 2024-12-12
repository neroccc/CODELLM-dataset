import json
import random


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        dp = [0] * (n + 1)

        # Set base cases
        for i in [1, 2, 3]:
            dp[i] = i

        for num in range(4, n + 1):
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp[num - i])

            dp[num] = ans

        return dp[n]


def generate_test_cases(num_cases=100, max_n=58):
    """
    Generates test cases for the integerBreak function.

    :param num_cases: Number of test cases to generate.
    :param max_n: Maximum value for n.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize n value within the valid range
        n = random.randint(2, max_n)

        # Calculate the expected output using the provided solution
        expected_output = solution.integerBreak(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })

    return test_cases


def save_test_cases_to_file(test_cases, filename="test_cases_343.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)


if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_n=58)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
