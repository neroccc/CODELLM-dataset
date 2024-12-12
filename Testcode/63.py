import json
import random
from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, m):
            obstacleGrid[i][0] = int(
                obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1
            )

        for j in range(1, n):
            obstacleGrid[0][j] = int(
                obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1
            )

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = (
                        obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                    )
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[m - 1][n - 1]

def generate_test_cases(num_cases=100, max_m=100, max_n=100):
    """
    Generates test cases for the uniquePathsWithObstacles function.

    :param num_cases: Number of test cases to generate.
    :param max_m: Maximum number of rows in the grid.
    :param max_n: Maximum number of columns in the grid.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        m = random.randint(1, max_m)
        n = random.randint(1, max_n)
        obstacle_grid = [[random.choice([0, 1]) for _ in range(n)] for _ in range(m)]

        # Ensure start and end points are not obstacles
        obstacle_grid[0][0] = 0
        obstacle_grid[m - 1][n - 1] = 0

        # Calculate expected output using the provided solution
        expected_output = solution.uniquePathsWithObstacles([row[:] for row in obstacle_grid])

        # Add test case
        test_cases.append({
            "input": obstacle_grid,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_63.json"):
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
    test_cases = generate_test_cases(num_cases=num_cases, max_m=100, max_n=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
