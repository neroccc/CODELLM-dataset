import json
import random
import string

class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[-1] * n for _ in range(n)]

        def util(i, j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            answer = 1 + util(i + 1, j)
            for k in range(i + 1, j + 1):
                if s[k] == s[i]:
                    answer = min(answer, util(i, k - 1) + util(k + 1, j))

            dp[i][j] = answer
            return answer

        return util(0, n - 1)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string of length between 1 and 100
        length = random.randint(1, 100)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        # Compute the output using the solution's method
        output = solution.strangePrinter(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_664.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
