import json
import random
from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [[0 for _ in range(len(stones))] for _ in range(len(stones))]  # DP table n x n
        run_sum = [0]  # Running sum -> sum [i..j] = run_sum[j] - run_sum[i]
        s = 0

        for i in stones:
            s += i
            run_sum.append(s)

        n = len(stones)

        for k in range(1, n):  # No. of stones left
            for i in range(0, n - k):  # From each starting point
                remove_i_stone = (run_sum[i + k + 1] - run_sum[i + 1])  # Score after removing i-th stone
                remove_j_stone = (run_sum[i + k] - run_sum[i])  # Score after removing j-th stone

                if (n - (k + 1)) % 2 == 0:  # Alice's move
                    dp[i][i + k] = max(remove_i_stone + dp[i + 1][i + k],
                                       remove_j_stone + dp[i][i + k - 1])
                else:  # Bob's move
                    dp[i][i + k] = min(-remove_i_stone + dp[i + 1][i + k],
                                       -remove_j_stone + dp[i][i + k - 1])

        return dp[0][n - 1]


# Helper function to generate random stone values
def generate_random_stones(n, max_value=1000):
    return [random.randint(1, max_value) for _ in range(n)]


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(2, 1000)
        stones = generate_random_stones(n)
        expected_output = solution.stoneGameVII(stones)

        test_cases.append({
            "input": {"stones": stones},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1690.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
