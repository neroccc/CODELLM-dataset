import json
import random
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        f = lambda x: sum(ch < x for ch in digits)
        d, k = len(digits), len(str(n))
        ans = k - 1 if d == 1 else (d ** k - d) // (d - 1)

        for i, ch in enumerate(str(n)):
            ans += f(ch) * (d ** (k - i - 1))
            if ch not in digits:
                break
        else:
            ans += 1

        return ans


def generate_test_cases(num_cases=100):
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        # Generate random values for digits and n
        digits_length = random.randint(1, 9)
        digits = sorted(random.sample([str(i) for i in range(1, 10)], digits_length))
        n = random.randint(1, 10 ** 9)

        # Compute the output using the solution's method
        output = solution.atMostNGivenDigitSet(digits, n)
        # Append the test case
        test_cases.append({
            "input": {
                "digits": digits,
                "n": n
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_902.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
