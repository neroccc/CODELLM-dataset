import json
import random

class Solution:
    def __init__(self):
        self.optionA = [100, 75, 50, 25]
        self.optionB = [0, 25, 50, 75]

    def solve(self, a, b, dp):
        if a == 0 and b == 0:
            return 0.5  # half the probability that A and B become empty at the same time
        if a == 0:
            return 1
        if b == 0:
            return 0

        if dp[a][b] != -1:
            return dp[a][b]

        ans = 0
        for k in range(4):
            rema = a - self.optionA[k]
            remb = b - self.optionB[k]
            ans += 0.25 * self.solve(max(0, rema), max(0, remb), dp)

        dp[a][b] = ans
        return ans

    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        return self.solve(n, n, dp)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random n value between 0 and 10^9
        n = random.randint(0, 10**9)
        # Compute the output using the solution's method
        output = solution.soupServings(n)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_808.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
