import random
import json
from typing import List
from functools import cache


class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        freq = [0] * 31
        for x in nums: freq[x] += 1

        masks = [0] * 31
        for x in range(1, 31):
            if x == 1:
                masks[x] = 0b10
            else:
                bits = 0
                xx = x
                for k in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
                    while xx % k == 0:
                        if (bits >> k) & 1: break  # repeated factors
                        bits ^= 1 << k
                        xx //= k
                    else:
                        continue
                    break
                else:
                    masks[x] = bits

        @cache
        def fn(x, m):
            """Return number of good subsets."""
            if x == 31: return int(m > 2)
            ans = fn(x + 1, m)
            if freq[x] and masks[x]:
                if x == 1:
                    ans *= 2 ** freq[x]
                elif not m & masks[x]:
                    ans += freq[x] * fn(x + 1, m | masks[x])
            return ans % 1_000_000_007

        return fn(1, 0)


# Function to generate random test inputs
def generate_random_test_case() -> List[int]:
    n = random.randint(1, 10 ** 5)  # Random size within constraints
    return [random.randint(1, 30) for _ in range(n)]


# Generate test cases and compute expected outputs
def generate_test_cases(num_cases: int = 100):
    solution = Solution()
    test_cases = []
    for _ in range(num_cases):
        test_input = generate_random_test_case()
        expected_output = solution.numberOfGoodSubsets(test_input)
        test_cases.append({
            "input": test_input,
            "output": expected_output
        })
    return test_cases


# Generate and save test cases to a JSON file
if __name__ == "__main__":
    test_cases = generate_test_cases()
    with open("test_cases_1994.json", "w") as f:
        json.dump(test_cases, f, indent=2)
