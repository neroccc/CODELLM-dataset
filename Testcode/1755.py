import json
import random
from typing import List
from bisect import bisect_left


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def fn(nums):
            ans = {0}
            for x in nums:
                ans |= {x + y for y in ans}
            return ans

        nums0 = sorted(fn(nums[:len(nums) // 2]))

        ans = float('inf')
        for x in fn(nums[len(nums) // 2:]):
            k = bisect_left(nums0, goal - x)
            if k < len(nums0): ans = min(ans, nums0[k] + x - goal)
            if 0 < k: ans = min(ans, goal - x - nums0[k - 1])
        return ans


# Helper function to generate random nums array
def generate_random_nums(length, value_range=(-10 ** 7, 10 ** 7)):
    return [random.randint(*value_range) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums_length = random.randint(1, 40)
        nums = generate_random_nums(nums_length)
        goal = random.randint(-10 ** 9, 10 ** 9)
        expected_output = solution.minAbsDifference(nums, goal)

        test_cases.append({
            "input": {"nums": nums, "goal": goal},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1755.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
