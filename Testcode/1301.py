import json
import random
from typing import List
from functools import lru_cache


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        matrix = []

        for i in board:
            matrix += [list(i)]

        m, n, mod = len(matrix), len(matrix[0]), 10**9 + 7

        @lru_cache(None)
        def dfs(i, j):
            if i >= m or j >= n or matrix[i][j] == "X":
                return (float("-inf"), 0)

            if i == m - 1 and j == n - 1:
                return (0, 1)

            op1 = dfs(i + 1, j)
            op2 = dfs(i, j + 1)
            op3 = dfs(i + 1, j + 1)

            score = int(matrix[i][j]) if matrix[i][j] != "E" else 0

            count, prev_score = 0, max(op1[0], op2[0], op3[0])

            if op1[0] == prev_score:
                count += op1[1]
            if op2[0] == prev_score:
                count += op2[1]
            if op3[0] == prev_score:
                count += op3[1]

            return (score + prev_score, count % mod)

        res = dfs(0, 0)

        return [max(res[0], 0), res[1]]


def generate_random_board(size_min=2, size_max=100):
    """Generate a random square board with characters."""
    size = random.randint(size_min, size_max)
    board = [["X" if random.random() < 0.3 else str(random.randint(1, 9)) for _ in range(size)] for _ in range(size)]
    board[0][0] = "E"
    board[-1][-1] = "S"
    return ["".join(row) for row in board]


def generate_test_cases(num_cases=50, max_size=10):
    """Generate test cases for the Paths with Maximum Score problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        board = generate_random_board(2, max_size)
        expected_output = solution.pathsWithMaxScore(board)
        test_cases.append({"input": board, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": ["E23", "2X2", "12S"], "output": solution.pathsWithMaxScore(["E23", "2X2", "12S"])},
        {"input": ["E12", "1X1", "21S"], "output": solution.pathsWithMaxScore(["E12", "1X1", "21S"])},
        {"input": ["E11", "XXX", "11S"], "output": solution.pathsWithMaxScore(["E11", "XXX", "11S"])},
        {"input": ["E1S"], "output": solution.pathsWithMaxScore(["E1S"])},
        {"input": ["E1", "1S"], "output": solution.pathsWithMaxScore(["E1", "1S"])},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_size = 10  # Limit board size for faster generation
    test_cases = generate_test_cases(num_cases, max_size)
    save_test_cases("../test_cases_1301.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'paths_with_max_score_test_cases.json'.")
