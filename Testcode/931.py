import json
import random
from typing import List

class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        if m == 1 or n == 1:
            return A[0][0]

        dp = [[float('inf')] * n for _ in range(m)]
        ans = float('inf')

        for i in range(len(A)):
            ans = min(ans, self.minFallingPathSumHelper(A, 0, i, dp))

        return ans

    def minFallingPathSumHelper(self, A, row, col, dp):
        m, n = len(A), len(A[0])

        if dp[row][col] != float('inf'):
            return dp[row][col]

        if row == m - 1:
            return A[row][col]

        left = right = float('inf')

        if col > 0:
            left = self.minFallingPathSumHelper(A, row + 1, col - 1, dp)

        straight = self.minFallingPathSumHelper(A, row + 1, col, dp)

        if col < n - 1:
            right = self.minFallingPathSumHelper(A, row + 1, col + 1, dp)

        dp[row][col] = min(left, min(straight, right)) + A[row][col]

        return dp[row][col]

# Test case generation
def generate_matrix(n, min_val, max_val):
    """Generate a random nxn matrix with values in range [min_val, max_val]."""
    return [[random.randint(min_val, max_val) for _ in range(n)] for _ in range(n)]

def generate_test_cases(num_cases=1000, max_n=100, min_val=-100, max_val=100):
    """Generate test cases for the minFallingPathSum problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        matrix = generate_matrix(n, min_val, max_val)
        expected_output = solution.minFallingPathSum(matrix)
        test_cases.append({"input": matrix, "output": expected_output})

    return test_cases

def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)

# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    test_cases = generate_test_cases(num_cases)
    save_test_cases("test_cases_931.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'test_case_.json'")
