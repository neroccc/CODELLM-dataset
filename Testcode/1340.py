import json
import random
from typing import List
from collections import defaultdict


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = defaultdict(int)

        def dfs(i):
            if i in dp:
                return dp[i]
            m_path = 0
            for j in range(i + 1, i + d + 1):
                if j >= len(arr) or arr[j] >= arr[i]:
                    break
                m_path = max(m_path, dfs(j))

            for j in range(i - 1, i - d - 1, -1):
                if j < 0 or arr[j] >= arr[i]:
                    break
                m_path = max(m_path, dfs(j))

            dp[i] = m_path + 1
            return dp[i]

        res = 0
        for i in range(len(arr)):
            res = max(res, dfs(i))
        return res


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the length of the array
        length = random.randint(1, 1000)
        # Generate a random array with values between 1 and 10^5
        arr = [random.randint(1, 10 ** 5) for _ in range(length)]
        # Choose a random jump distance
        d = random.randint(1, length)
        # Compute the expected output using the solution
        expected_output = solution.maxJumps(arr, d)
        # Add the test case to the list
        test_cases.append({"input":{"arr": arr, "d": d}, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1340.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 1000 test cases
generate_test_cases()
