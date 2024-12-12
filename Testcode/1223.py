import json
import random
from typing import List
from functools import lru_cache

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def func(idx, prevNum, prevNumFreq):
            if idx == n:
                return 1

            ans = 0
            for i in range(1, 7):
                if i == prevNum:
                    if prevNumFreq < rollMax[i - 1]:
                        ans += func(idx + 1, i, prevNumFreq + 1)

                else:
                    ans += func(idx + 1, i, 1)

            return ans % MOD

        return func(0, 0, 0)


def generate_random_rollMax():
    """Generate a random rollMax array of length 6."""
    return [random.randint(1, 15) for _ in range(6)]


def generate_test_cases(num_cases=50, max_n=50):
    """Generate test cases for the Dice Roll Simulator problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        rollMax = generate_random_rollMax()
        expected_output = solution.dieSimulator(n, rollMax)
        test_cases.append({"input": {"n": n, "rollMax": rollMax}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"n": 2, "rollMax": [1, 1, 2, 2, 2, 3]}, "output": solution.dieSimulator(2, [1, 1, 2, 2, 2, 3])},
        {"input": {"n": 2, "rollMax": [1, 1, 1, 1, 1, 1]}, "output": solution.dieSimulator(2, [1, 1, 1, 1, 1, 1])},
        {"input": {"n": 3, "rollMax": [1, 1, 1, 2, 2, 3]}, "output": solution.dieSimulator(3, [1, 1, 1, 2, 2, 3])},
        {"input": {"n": 10, "rollMax": [15, 15, 15, 15, 15, 15]}, "output": solution.dieSimulator(10, [15, 15, 15, 15, 15, 15])},
        {"input": {"n": 1, "rollMax": [1, 1, 1, 1, 1, 1]}, "output": solution.dieSimulator(1, [1, 1, 1, 1, 1, 1])},
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
    max_n = 50  # Limit max_n to 50 for faster generation
    test_cases = generate_test_cases(num_cases, max_n)
    save_test_cases("../test_cases_1223.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'dice_roll_simulator_test_cases.json'.")
