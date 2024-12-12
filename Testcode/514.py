import json
import random
from typing import List


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = {}

        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(key):
                return 0
            ans = float('inf')
            for k in range(len(ring)):
                if ring[k] == key[j]:
                    delta = abs(k - i)
                    steps = min(delta, len(ring) - delta)
                    ans = min(ans, steps + dp(k, j + 1))
            memo[(i, j)] = ans
            return ans

        return dp(0, 0) + len(key)


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate random `ring` and `key` strings
        ring_length = random.randint(1, 100)  # 1 <= ring.length <= 100
        key_length = random.randint(1, 100)  # 1 <= key.length <= 100
        ring = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=ring_length))
        key = ''.join(random.choices(ring, k=key_length))  # Ensure key is a subset of ring

        # Calculate expected output using the provided solution
        expected_output = solution.findRotateSteps(ring, key)

        # Add test case
        test_cases.append({
            "input": {"ring": ring, "key": key},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_514.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
