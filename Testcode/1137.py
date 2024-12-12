import json
import random


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next
        return t2


def generate_test_cases(num_cases=50):
    """Generate test cases for the Tribonacci Sequence problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(0, 37)
        expected_output = solution.tribonacci(n)
        test_cases.append({"input": n, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": 0, "output": solution.tribonacci(0)},
        {"input": 1, "output": solution.tribonacci(1)},
        {"input": 2, "output": solution.tribonacci(2)},
        {"input": 3, "output": solution.tribonacci(3)},
        {"input": 25, "output": solution.tribonacci(25)},
        {"input": 37, "output": solution.tribonacci(37)},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 50
    test_cases = generate_test_cases(num_cases)
    save_test_cases("test_cases_1137.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'tribonacci_test_cases.json'.")
