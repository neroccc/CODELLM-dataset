import json
import random
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [0 for _ in range(len(grid[0]))]
        for i in range(len(grid) - 1, -1, -1):
            for j in range(len(grid[0]) - 1, -1, -1):
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + dp[j + 1]
                elif j == len(grid[0]) - 1 and i != len(grid) - 1:
                    dp[j] = grid[i][j] + dp[j]
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[j] = grid[i][j] + min(dp[j], dp[j + 1])
                else:
                    dp[j] = grid[i][j]
        return dp[0]

def generate_test_cases(num_cases=100, max_m=200, max_n=200, max_value=200):
    """
    Generates test cases for the minPathSum function.

    :param num_cases: Number of test cases to generate.
    :param max_m: Maximum number of rows in the grid.
    :param max_n: Maximum number of columns in the grid.
    :param max_value: Maximum value for grid elements.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the grid dimensions and values
        m = random.randint(1, max_m)
        n = random.randint(1, max_n)
        grid = [[random.randint(0, max_value) for _ in range(n)] for _ in range(m)]
        # Calculate the expected output using the provided solution
        expected_output = solution.minPathSum(grid)

        # Add test case
        test_cases.append({
            "input": grid,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_64.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 100
    test_cases = generate_test_cases(num_cases=num_cases, max_m=200, max_n=200, max_value=200)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
