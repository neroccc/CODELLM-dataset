import json
import random
from collections import defaultdict
from typing import List
from math import inf


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        freq = defaultdict(lambda: defaultdict(int))
        for i, x in enumerate(nums):
            freq[i % k][x] += 1  # Frequency by modulo index

        n = 1 << 10
        dp = [0] + [-inf] * (n - 1)
        for i in range(k):
            mx = max(dp)
            tmp = [0] * n
            for x, c in enumerate(dp):
                for xx, cc in freq[i].items():
                    tmp[x ^ xx] = max(tmp[x ^ xx], c + cc, mx)
            dp = tmp
        return len(nums) - dp[0]


# Helper function to generate random test cases
def generate_random_case(max_len, max_val=1023):
    nums_len = random.randint(1, max_len)
    nums = [random.randint(0, max_val) for _ in range(nums_len)]
    k = random.randint(1, nums_len)
    return nums, k


# Generate test cases
def generate_test_cases(num_cases=100, max_len=2000):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        nums, k = generate_random_case(max_len)
        expected_output = solution.minChanges(nums, k)

        test_cases.append({
            "input": {"nums": nums, "k": k},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1787.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
generate_test_cases()
