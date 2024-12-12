import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def maxHappyGroups(self, batchSize: int, groups: List[int]) -> int:
        @lru_cache(None)
        def dp(counter_tup, mod):
            if sum(counter_tup) == 0:
                return 0
            counter = list(counter_tup)
            startNewBatch = (mod == 0)
            res = 0
            for i in range(len(counter)):
                if counter[i] != 0:
                    counter[i] -= 1
                    mod2 = (mod - i) % batchSize
                    nxt_res = dp(tuple(counter), mod2) + startNewBatch
                    res = max(res, nxt_res)
                    counter[i] += 1
            return res

        counter = [0] * batchSize
        for g in groups:
            counter[g % batchSize] += 1
        return dp(tuple(counter), 0)

# Helper function to generate random test cases
def generate_random_case(batch_size_max=9, groups_max_len=30, group_max_value=10**9):
    batchSize = random.randint(1, batch_size_max)
    groups_len = random.randint(1, groups_max_len)
    groups = [random.randint(1, group_max_value) for _ in range(groups_len)]
    return batchSize, groups

# Generate test cases
def generate_test_cases(num_cases=50):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        batchSize, groups = generate_random_case()
        expected_output = solution.maxHappyGroups(batchSize, groups)

        test_cases.append({
            "input": {"batchSize": batchSize, "groups": groups},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1815.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save test cases
generate_test_cases()
