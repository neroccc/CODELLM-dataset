import json
import random

class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0

        for r in range(N):
            count = 0
            for c in range(N):
                count = 0 if (r, c) in banned else count + 1
                dp[r][c] = count

            count = 0
            for c in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

        for c in range(N):
            count = 0
            for r in range(N):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count

            count = 0
            for r in range(N - 1, -1, -1):
                count = 0 if (r, c) in banned else count + 1
                if count < dp[r][c]:
                    dp[r][c] = count
                if dp[r][c] > ans:
                    ans = dp[r][c]

        return ans


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate random grid size N between 1 and 500
        N = random.randint(1, 500)
        # Generate random mines count between 1 and min(5000, N*N)
        mines_count = random.randint(1, min(5000, N * N))
        # Generate unique mines positions
        mines = [random.sample(range(N), 2) for _ in range(mines_count)]
        # Compute the output using the solution's method
        output = solution.orderOfLargestPlusSign(N, mines)
        # Append the test case
        test_cases.append({
            "input": {
                "N": N,
                "mines": mines
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_764.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
