import json
import random
from math import log
from functools import cache


class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:

        @cache
        def fn(val):
            """Return min ops to express val."""
            if val < x: return min(2 * val - 1, 2 * (x - val))
            k = int(log(val) // log(x))
            ans = k + fn(val - x ** k)
            if x ** (k + 1) < 2 * val:
                ans = min(ans, k + 1 + fn(x ** (k + 1) - val))
            return ans

        return fn(target)


def generate_test_cases(num_cases=50, max_x=100, max_target=200_000_000):
    """Generate test cases for the Least Number of Operators to Express Target problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        x = random.randint(2, max_x)
        target = random.randint(1, max_target)
        expected_output = solution.leastOpsExpressTarget(x, target)
        test_cases.append({"input": {"x": x, "target": target}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"x": 3, "target": 19}, "output": solution.leastOpsExpressTarget(3, 19)},
        {"input": {"x": 5, "target": 501}, "output": solution.leastOpsExpressTarget(5, 501)},
        {"input": {"x": 100, "target": 100000000}, "output": solution.leastOpsExpressTarget(100, 100000000)},
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
    max_x = 100
    max_target = 200_000_000
    test_cases = generate_test_cases(num_cases, max_x, max_target)
    save_test_cases("test_cases_964.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'least_ops_to_express_target_test_cases.json'.")
