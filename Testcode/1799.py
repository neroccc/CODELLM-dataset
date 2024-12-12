import json
import random
from math import gcd
from functools import lru_cache
from itertools import combinations
from typing import List


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @lru_cache(None)
        def fn(nums, k):
            if not nums:
                return 0
            ans = 0
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    rest = nums[:i] + nums[i + 1:j] + nums[j + 1:]
                    ans = max(ans, k * gcd(nums[i], nums[j]) + fn(tuple(rest), k + 1))
            return ans

        return fn(tuple(nums), 1)


# Helper function to generate random test cases
def generate_random_case(n, max_val=10 ** 6):
    nums = [random.randint(1, max_val) for _ in range(2 * n)]
    return nums


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, 7)  # Random n between 1 and 7
        nums = generate_random_case(n)
        expected_output = solution.maxScore(nums)

        test_cases.append({
            "input": {"nums": nums},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1799.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
generate_test_cases()
