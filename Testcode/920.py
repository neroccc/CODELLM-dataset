import json
import random

class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0 for _ in range(n + 1)] for _ in range(2)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            dp[i % 2][0] = 0
            for j in range(1, min(i, n) + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] * (n - (j - 1)) % MOD
                if j > k:
                    dp[i % 2][j] = (dp[i % 2][j] + dp[(i - 1) % 2][j] * (j - k)) % MOD

        return dp[goal % 2][n]

def generate_test_cases(num_cases=10):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate random values for n, goal, and k
        n = random.randint(1, 100)  # Number of unique songs
        goal = random.randint(n, 100)  # Total number of songs in the playlist (at least n)
        k = random.randint(0, n - 1)  # Minimum number of other songs before repetition

        # Calculate the expected output using the solution
        output = solution.numMusicPlaylists(n, goal, k)

        # Append the test case
        test_cases.append({
            "input": {"n": n, "goal": goal, "k": k},
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_920.json", "w") as file:
        json.dump(test_cases, file, indent=4)

# Generate the test cases
generate_test_cases(num_cases=100)
