import json
import random
from math import perm

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        digits = list(map(int, str(n + 1)))
        nl = len(digits)
        res = sum(9 * perm(9, i) for i in range(nl - 1))
        s = set()
        for i, x in enumerate(digits):
            for y in range(i == 0, x):
                if y not in s:
                    res += perm(9 - i, nl - i - 1)
            if x in s:
                break
            s.add(x)
        return n - res


def generate_test_cases(num_cases=50, max_n=10**9):
    """Generate test cases for the Numbers with Repeated Digits problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        expected_output = solution.numDupDigitsAtMostN(n)
        test_cases.append({"input": n, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": 20, "output": solution.numDupDigitsAtMostN(20)},
        {"input": 100, "output": solution.numDupDigitsAtMostN(100)},
        {"input": 1000, "output": solution.numDupDigitsAtMostN(1000)},
        {"input": 1, "output": solution.numDupDigitsAtMostN(1)},
        {"input": 10**9, "output": solution.numDupDigitsAtMostN(10**9)},
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
    max_n = 10**9
    test_cases = generate_test_cases(num_cases, max_n)
    save_test_cases("../test_cases_1012.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'num_dup_digits_test_cases.json'.")
