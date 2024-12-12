import json
import random
from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        presum, res = 0, 0
        for i in range(n):
            presum += satisfaction[i]
            if presum < 0:
                break
            res += presum
        return res


# Generate test cases
def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Randomly decide the number of dishes
        n = random.randint(1, 500)
        # Generate random satisfaction levels
        satisfaction = [random.randint(-1000, 1000) for _ in range(n)]
        # Compute the expected output using the solution
        expected_output = solution.maxSatisfaction(satisfaction)
        # Add the test case to the list
        test_cases.append({"satisfaction": satisfaction, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1402.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate 100 test cases
generate_test_cases()
