import json
import random
from typing import List
import functools


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:

        @functools.lru_cache(None)
        def dfs(i, k):
            if k == 1:
                return sum(nums[i:]) / len(nums[i:])  # Calculate sum for the remaining elements

            maxAvg = 0

            for j in range(i + 1, len(nums)):  # Try partitioning at each index and calculate average
                avg = sum(nums[i:j]) / len(nums[i:j])
                subarrayAvg = avg + dfs(j, k - 1)  # Call with the next index (j) after partition
                maxAvg = max(maxAvg, subarrayAvg)

            return maxAvg

        return dfs(0, k)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random array length between 1 and 100
        length = random.randint(1, 100)
        # Generate random elements for nums in the range [1, 10^4]
        nums = [random.randint(1, 10000) for _ in range(length)]
        # Generate a random k value between 1 and the length of nums
        k = random.randint(1, length)
        # Compute the output using the solution's method
        output = solution.largestSumOfAverages(nums, k)
        # Append the test case
        test_cases.append({
            "input": {
                "nums": nums,
                "k": k
            },
            "output": round(output, 6)  # Round to 6 decimal places for precision
        })

    # Save to a JSON file
    with open("test_cases_813.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
