import json
import random
from functools import lru_cache

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        n = bin(n)[2:]
        if '1' not in n:
            return 0
        n = tuple(list(n))

        @lru_cache(None)
        def zero(n):  # Min operations to transform n to all 0 bits
            n = list(n)
            if all(bit == '0' for bit in n):
                return 0
            if n[0] == '0':
                if len(n) == 1:
                    return 0
                else:
                    return zero(tuple(n[1:]))
            else:
                if len(n) == 1:
                    return 1
                else:
                    ops = one(tuple(n[1:])) + 1
                    nei = ['0' for _ in range(len(n) - 1)]
                    nei[0] = '1'
                    return ops + zero(tuple(nei))

        @lru_cache(None)
        def one(n):  # Min operations to transform n to first bit 1 and all other bits 0
            n = list(n)
            if n[0] == '1' and all(bit == '0' for bit in n[1:]):
                return 0
            if n[0] == '1':
                if len(n) == 1:
                    return 0
                else:
                    return zero(tuple(n[1:]))
            else:
                if len(n) == 1:
                    return 1
                else:
                    ops = one(tuple(n[1:])) + 1
                    nei = ['0' for _ in range(len(n) - 1)]
                    nei[0] = '1'
                    return ops + zero(tuple(nei))
        return zero(n)

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(0, 10**9)
        expected_output = solution.minimumOneBitOperations(n)

        test_cases.append({
            "input": {"n": n},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1611.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
