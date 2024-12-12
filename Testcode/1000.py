import json
import random
from typing import List
from functools import cache
from math import inf

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones) - 1) % (k - 1):
            return -1  # impossible

        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        @cache
        def fn(lo, hi):
            """Return min cost of merging stones[lo:hi]."""
            if hi - lo < k:
                return 0  # not enough stones
            ans = inf
            for mid in range(lo + 1, hi, k - 1):
                ans = min(ans, fn(lo, mid) + fn(mid, hi))
            if (hi - lo - 1) % (k - 1) == 0:
                ans += prefix[hi] - prefix[lo]
            return ans

        return fn(0, len(stones))


def generate_random_stones_and_k(max_length=30, max_stone=100):
    """Generate a random stones array and k value."""
    length = random.randint(1, max_length)
    stones = [random.randint(1, max_stone) for _ in range(length)]
    k = random.randint(2, max_length)
    return stones, k


def generate_test_cases(num_cases=50, max_length=30, max_stone=100):
    """Generate test cases for the Minimum Cost to Merge Stones problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        stones, k = generate_random_stones_and_k(max_length, max_stone)
        expected_output = solution.mergeStones(stones, k)
        test_cases.append({"input": {"stones": stones, "k": k}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"stones": [3, 2, 4, 1], "k": 2}, "output": solution.mergeStones([3, 2, 4, 1], 2)},
        {"input": {"stones": [3, 2, 4, 1], "k": 3}, "output": solution.mergeStones([3, 2, 4, 1], 3)},
        {"input": {"stones": [3, 5, 1, 2, 6], "k": 3}, "output": solution.mergeStones([3, 5, 1, 2, 6], 3)},
        {"input": {"stones": [1, 1, 1, 1], "k": 2}, "output": solution.mergeStones([1, 1, 1, 1], 2)},
        {"input": {"stones": [1, 1, 1, 1], "k": 4}, "output": solution.mergeStones([1, 1, 1, 1], 4)},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    test_cases = generate_test_cases(num_cases)
    save_test_cases("test_cases_1000.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'merge_stones_test_cases.json'.")
