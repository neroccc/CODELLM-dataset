import json
import random
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans


# Helper function to generate random binary arrays
def generate_binary_array(length):
    return [random.randint(0, 1) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10 ** 5)
        nums = generate_binary_array(length)

        # Compute expected output using the provided solution
        expected_output = solution.longestSubarray(nums)

        test_cases.append({
            "input": {"nums": nums},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1493.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
