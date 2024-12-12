import json
import random
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n)]
        suffix_sum = [0] * n
        suffix_sum[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        for i in range(n - 1, -1, -1):
            for m in range(1, n + 1):
                if i + 2 * m >= n:
                    dp[i][m] = suffix_sum[i]
                else:
                    for x in range(1, 2 * m + 1):
                        dp[i][m] = max(dp[i][m], suffix_sum[i] - dp[i + x][max(m, x)])

        return dp[0][1]


def generate_random_piles(min_length=1, max_length=100, max_value=10 ** 4):
    """Generate a random list of piles."""
    length = random.randint(min_length, max_length)
    return [random.randint(1, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=100, max_value=10 ** 4):
    """Generate test cases for the Stone Game II problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        piles = generate_random_piles(1, max_length, max_value)
        expected_output = solution.stoneGameII(piles)
        test_cases.append({
            "input": piles,
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": [2, 7, 9, 4, 4], "output": solution.stoneGameII([2, 7, 9, 4, 4])},
        {"input": [1, 2, 3, 4, 5, 100], "output": solution.stoneGameII([1, 2, 3, 4, 5, 100])},
        {"input": [1], "output": solution.stoneGameII([1])},
        {"input": [10 ** 4] * 100, "output": solution.stoneGameII([10 ** 4] * 100)},
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
    max_length = 100
    max_value = 10 ** 4
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("test_cases_1140.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'stone_game_ii_test_cases.json'.")
