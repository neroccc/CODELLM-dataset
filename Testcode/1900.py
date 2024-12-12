import json
import random
from itertools import product
from functools import cache
from math import inf


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int):
        firstPlayer, secondPlayer = firstPlayer - 1, secondPlayer - 1  # 0-indexed

        @cache
        def fn(k, mask):
            """Return earliest and latest rounds."""
            from collections import deque
            can = deque()
            for i in range(n):
                if mask & (1 << i): can.append(i)

            cand = []  # eliminated player
            while len(can) > 1:
                p1, p2 = can.popleft(), can.pop()
                if p1 == firstPlayer and p2 == secondPlayer or p1 == secondPlayer and p2 == firstPlayer:
                    return [k, k]  # game of interest
                if p1 in (firstPlayer, secondPlayer):
                    cand.append([p2])  # p2 eliminated
                elif p2 in (firstPlayer, secondPlayer):
                    cand.append([p1])  # p1 eliminated
                else:
                    cand.append([p1, p2])  # both could be eliminated

            minn, maxx = inf, -inf
            for x in product(*cand):
                mask0 = mask
                for i in x: mask0 ^= 1 << i
                mn, mx = fn(k + 1, mask0)
                minn = min(minn, mn)
                maxx = max(maxx, mx)
            return minn, maxx

        return fn(1, (1 << n) - 1)


def generate_test_cases(num_cases=100):
    """Generate random test cases for the tournament problem."""
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(2, 28)  # n ranges between 2 and 28
        firstPlayer = random.randint(1, n - 1)
        secondPlayer = random.randint(firstPlayer + 1, n)
        test_cases.append((n, firstPlayer, secondPlayer))
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute expected outputs using the provided solution."""
    solution = Solution()
    outputs = []
    for n, firstPlayer, secondPlayer in test_cases:
        output = solution.earliestAndLatest(n, firstPlayer, secondPlayer)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases()

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": {"n": n, "firstPlayer": firstPlayer, "secondPlayer": secondPlayer},
              "output": output} for (n, firstPlayer, secondPlayer), output in
             zip(test_cases, expected_outputs)]

with open("test_cases_1900.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
