import json
import random
from itertools import accumulate
from bisect import bisect_left
from functools import cache


class Solution:
    def stoneGameV(self, stoneValue):
        sv = [0, *accumulate(stoneValue)]

        @cache
        def helper(fro, to):
            if to - fro == 1:
                return 0

            mid = bisect_left(sv, (sv[to] + sv[fro]) // 2)

            dist = res = 0
            explore_more = True
            while explore_more:
                explore_more = False
                for i in [mid - dist, mid + dist]:
                    if fro < i <= to:
                        left, right = sv[i] - sv[fro], sv[to] - sv[i]
                        if res // 2 <= left <= right:
                            res = max(res, left + helper(fro, i))
                            explore_more = True
                        if left >= right >= res // 2:
                            res = max(res, right + helper(i, to))
                            explore_more = True
                dist += 1
            return res

        return helper(0, len(stoneValue))


# Helper function to generate random stone values
def generate_random_stone_values(length, max_value=10 ** 6):
    return [random.randint(1, max_value) for _ in range(length)]


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 500)
        stoneValue = generate_random_stone_values(length)

        # Compute expected output using the provided solution
        expected_output = solution.stoneGameV(stoneValue)

        test_cases.append({
            "input": {"stoneValue": stoneValue},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1563.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
