import json
import random
from typing import List

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for k in range(2, n):
            for i in range(n - k):
                start, end = i, i + k
                dp[start][end] = float("inf")
                for j in range(start + 1, end):
                    dp[start][end] = min(dp[start][end], dp[start][j] + dp[j][end] + A[start] * A[end] * A[j])
        return dp[0][-1]


def generate_random_polygon(min_vertices=3, max_vertices=50, max_value=100):
    """Generate a random convex polygon represented as a list of vertex values."""
    num_vertices = random.randint(min_vertices, max_vertices)
    return [random.randint(1, max_value) for _ in range(num_vertices)]


def generate_test_cases(num_cases=50, max_vertices=50, max_value=100):
    """Generate test cases for the Minimum Score Triangulation of Polygon problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        values = generate_random_polygon(3, max_vertices, max_value)
        expected_output = solution.minScoreTriangulation(values)
        test_cases.append({"input": values, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [1, 2, 3], "output": solution.minScoreTriangulation([1, 2, 3])},
        {"input": [3, 7, 4, 5], "output": solution.minScoreTriangulation([3, 7, 4, 5])},
        {"input": [1, 3, 1, 4, 1, 5], "output": solution.minScoreTriangulation([1, 3, 1, 4, 1, 5])},
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
    max_vertices = 50
    max_value = 100
    test_cases = generate_test_cases(num_cases, max_vertices, max_value)
    save_test_cases("../test_cases_1039.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'min_score_triangulation_test_cases.json'.")
