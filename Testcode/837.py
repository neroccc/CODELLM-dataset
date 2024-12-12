import json
import random

class Solution:
    def new21Game(self, N, K, maxPts):
        # Corner cases
        if K == 0:
            return 1.0
        if N >= K - 1 + maxPts:
            return 1.0

        # dp[i] is the probability of getting point i.
        dp = [0.0] * (N + 1)

        probability = 0.0  # dp of N or less points.
        windowSum = 1.0  # Sliding required window sum
        dp[0] = 1.0
        for i in range(1, N + 1):
            dp[i] = windowSum / maxPts

            if i < K:
                windowSum += dp[i]
            else:
                probability += dp[i]

            if i >= maxPts:
                windowSum -= dp[i - maxPts]

        return probability


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate random values for N, K, and maxPts
        n = random.randint(0, 10000)
        k = random.randint(0, n)
        maxPts = random.randint(1, min(10000, 2 * (n + 1)))  # Ensure maxPts isn't unnecessarily large
        # Compute the output using the solution's method
        output = solution.new21Game(n, k, maxPts)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n,
                "k": k,
                "maxPts": maxPts
            },
            "output": round(output, 5)  # Round to 5 decimal places for precision
        })

    # Save to a JSON file
    with open("test_cases_837.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
