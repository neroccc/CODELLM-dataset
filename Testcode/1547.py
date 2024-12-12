import json
import random


class Solution:
    def minCost(self, n, cuts):
        cuts.append(0)
        cuts.append(n)
        cuts.sort()
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]

        for l in range(2, m):
            for i in range(m - l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cuts[j] - cuts[i])

        return dp[0][m - 1]


# Helper function to generate random cuts
def generate_cuts(n, num_cuts):
    return sorted(random.sample(range(1, n), num_cuts))


# Generate test cases
def generate_test_cases(num_cases=1000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(2, 10 ** 6)
        num_cuts = random.randint(1, min(n - 1, 100))
        cuts = generate_cuts(n, num_cuts)

        # Compute expected output using the provided solution
        expected_output = solution.minCost(n, cuts)

        test_cases.append({
            "input": {"n": n, "cuts": cuts},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1547.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
