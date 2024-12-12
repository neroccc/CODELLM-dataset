import json
import random
from collections import defaultdict

class Solution:
    def numPermsDISequence(self, s: str) -> int:
        mem = defaultdict(int)

        def dfs(i, val=0):
            if i == len(s):
                return 1
            if (i, val) in mem:
                return mem[i, val]
            p = 0
            if s[i] == "D":
                for ind in range(0, val + 1):
                    p += dfs(i + 1, ind) % (10**9 + 7)
            else:
                for ind in range(val + 1, i + 2):
                    p += dfs(i + 1, ind) % (10**9 + 7)
            mem[i, val] = p
            return p

        return dfs(0) % (10**9 + 7)


def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate a random sequence of 'D' and 'I'
        n = random.randint(1, 20)  # Limit length to 20 for practical computation
        s = ''.join(random.choice(['D', 'I']) for _ in range(n))

        # Compute the output using the solution's method
        output = solution.numPermsDISequence(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_903.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
