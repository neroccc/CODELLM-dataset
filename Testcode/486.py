import json
import random
from typing import List
from collections import defaultdict


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)

        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)

            memo[(left, right)] = max(score_by_left, score_by_right)
            return memo[(left, right)]

        return maxDiff(0, n - 1) >= 0


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate a random length for the nums array
        nums_length = random.randint(1, 20)  # Constraints: 1 <= nums.length <= 20
        nums = [random.randint(0, 10 ** 7) for _ in range(nums_length)]  # Random numbers in the array

        # Calculate expected output using the provided solution
        expected_output = solution.predictTheWinner(nums)

        # Add test case
        test_cases.append({
            "input": {"nums": nums},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_486.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
