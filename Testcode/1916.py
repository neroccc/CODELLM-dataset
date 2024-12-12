import json
import random
from collections import defaultdict
from math import comb
from typing import List


class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        tree = defaultdict(list)
        for i, x in enumerate(prevRoom):
            tree[x].append(i)

        def fn(n):
            """Return number of nodes and ways to build sub-tree."""
            if not tree[n]:
                return 1, 1  # leaf
            c, m = 0, 1
            for nn in tree[n]:
                cc, mm = fn(nn)
                c += cc
                m = (m * comb(c, cc) * mm) % 1_000_000_007
            return c + 1, m

        return fn(0)[1]


def generate_test_cases(num_cases=100, max_n=10 ** 5):
    """Generate test cases for the waysToBuildRooms problem."""
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(2, min(100, max_n))  # Keep test sizes practical
        prevRoom = [-1] + [random.randint(0, i - 1) for i in range(1, n)]
        test_cases.append(prevRoom)
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the given test cases."""
    solution = Solution()
    outputs = []
    for prevRoom in test_cases:
        output = solution.waysToBuildRooms(prevRoom)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=100, max_n=1000)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": prevRoom, "output": output} for prevRoom, output in zip(test_cases, expected_outputs)]

with open("test_cases_1916.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
