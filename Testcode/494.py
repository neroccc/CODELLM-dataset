import json
import random
from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        summ = sum(nums)
        if summ < abs(target) or (summ + target) & 1:
            return 0

        def knapsack(target: int) -> int:
            dp = [1] + [0] * summ
            for num in nums:
                for j in range(summ, num - 1, -1):
                    dp[j] += dp[j - num]
            return dp[target]

        return knapsack((summ + target) // 2)

def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate a random list of integers (nums)
        nums_length = random.randint(1, 20)  # Array size constrained to 1 <= nums.length <= 20
        nums = [random.randint(0, 1000) for _ in range(nums_length)]  # 0 <= nums[i] <= 1000

        # Generate a random target within the allowable range
        target = random.randint(-1000, 1000)

        # Calculate the expected output using the provided solution
        expected_output = solution.findTargetSumWays(nums, target)

        # Add test case
        test_cases.append({
            "input": {"nums": nums, "target": target},
            "output": expected_output
        })

    return test_cases

# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_494.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
