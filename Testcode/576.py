import json
from typing import List

class Solution:
    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:
        M = 1000000000 + 7
        dp = [[0] * n for _ in range(m)]
        dp[x][y] = 1
        count = 0

        for moves in range(1, N + 1):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + dp[i][j]) % M
                    if j == n - 1:
                        count = (count + dp[i][j]) % M
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M
                    temp[i][j] = (
                        ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % M +
                        ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % M
                    ) % M

            dp = temp

        return count


def generate_test_cases(num_cases=100):
    import random

    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Randomly generate the dimensions of the grid (1 to 50 as per constraints)
        m = random.randint(1, 50)
        n = random.randint(1, 50)
        # Randomly generate the maximum number of moves (0 to 50)
        maxMove = random.randint(0, 50)
        # Randomly generate the starting row and column
        startRow = random.randint(0, m - 1)
        startColumn = random.randint(0, n - 1)
        # Compute the output using the solution's method
        output = solution.findPaths(m, n, maxMove, startRow, startColumn)
        # Append the test case
        test_cases.append({
            "input": {
                "m": m,
                "n": n,
                "maxMove": maxMove,
                "startRow": startRow,
                "startColumn": startColumn
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_576.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
