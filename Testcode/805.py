import json
import random
from typing import List

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)

        if n == 1:
            return False

        def possible_sums(arr: List[int]) -> int:
            subset_sums = 1
            for a in arr:
                subset_sums |= (subset_sums << a)
            return (subset_sums - 1) ^ (1 << sum(arr))

        transformed_nums = [n * num - total_sum for num in nums]

        if 0 in transformed_nums:
            return True

        positives = [num for num in transformed_nums if num > 0]
        negatives = [-num for num in transformed_nums if num < 0]

        return bool(possible_sums(positives) & possible_sums(negatives))


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random length for nums between 1 and 30
        length = random.randint(1, 30)
        # Generate random elements for nums in the range [0, 10^4]
        nums = [random.randint(0, 10000) for _ in range(length)]
        # Compute the output using the solution's method
        output = solution.splitArraySameAverage(nums)
        # Append the test case
        test_cases.append({
            "input": {
                "nums": nums
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_805.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
