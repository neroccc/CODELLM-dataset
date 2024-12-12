import json
import random
from collections import defaultdict
from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        d = defaultdict(int)
        for i in range(1, 27): d[str(i)] = 1
        for i in range(10): d["*"+str(i)] = 1 + (i < 7)
        d['*'], d['**'], d['1*'], d['2*'] = 9, 15, 9, 6

        n, M = len(s) - 1, 10**9 + 7
        dp = [d[s[0]]] + [0] * n + [1]

        for i in range(n):
            one, two = s[i+1], s[i]+s[i+1]

            dp[i+1] = (d[one] * dp[i] +
                       d[two] * dp[i-1]) % M
            if not dp[i+1]: return 0

        return dp[-2]


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string of length between 1 and 10^5 with digits and '*'
        length = random.randint(1, 100)
        s = ''.join(random.choices('0123456789*', k=length))
        # Compute the output using the solution's method
        output = solution.numDecodings(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_639.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
