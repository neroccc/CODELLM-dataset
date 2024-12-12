import json
import random
import string

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # Prepare the two-dimensional array
        m, n = len(s1), len(s2)
        compute_cost = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the base case values
        for i in range(1, m + 1):
            compute_cost[i][0] = compute_cost[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            compute_cost[0][j] = compute_cost[0][j - 1] + ord(s2[j - 1])

        # Fill the remaining cells using the Bellman Equation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    compute_cost[i][j] = compute_cost[i - 1][j - 1]
                else:
                    compute_cost[i][j] = min(
                        ord(s1[i - 1]) + compute_cost[i - 1][j],
                        ord(s2[j - 1]) + compute_cost[i][j - 1]
                    )

        # Return the answer for entire input strings
        return compute_cost[m][n]


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate two random strings with lengths between 1 and 1000
        length1 = random.randint(1, 1000)
        length2 = random.randint(1, 1000)
        s1 = ''.join(random.choices(string.ascii_lowercase, k=length1))
        s2 = ''.join(random.choices(string.ascii_lowercase, k=length2))
        # Compute the output using the solution's method
        output = solution.minimumDeleteSum(s1, s2)
        # Append the test case
        test_cases.append({
            "input": {
                "s1": s1,
                "s2": s2
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_712.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
