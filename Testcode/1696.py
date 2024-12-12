import json
import random
from collections import deque
from typing import List

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        deq = deque()
        deq.append(0)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = nums[i] + dp[deq[0]]  # Maximum value in deque within that window
            if deq[0] < i - k + 1:
                deq.popleft()  # Check whether left bound is still accessible
            while deq and dp[deq[-1]] < dp[i]:
                deq.pop()  # Update deque with current i'th element
            deq.append(i)
        return dp[-1]  # Return total score

# Helper function to generate random nums array
def generate_random_nums(length, value_range=(-10**4, 10**4)):
    return [random.randint(*value_range) for _ in range(length)]

# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10**5)
        k = random.randint(1, length)
        nums = generate_random_nums(length)
        expected_output = solution.maxResult(nums, k)

        test_cases.append({
            "input": {"nums": nums, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1696.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
