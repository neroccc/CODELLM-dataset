import json
import random

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        if n == 2:
            return 0.5
        dp = [0] * (n + 1)
        dp[1] = 1.0
        dp[2] = 0.5
        acc = 1.5
        for i in range(3, n + 1):
            dp[i] = (1.0 / i) * acc
            acc += dp[i]
        return dp[-1]


def generate_test_cases(num_cases=50, max_n=1000):
    """Generate test cases for the Nth Person Gets Nth Seat problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        expected_output = solution.nthPersonGetsNthSeat(n)
        test_cases.append({"input": n, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": 1, "output": solution.nthPersonGetsNthSeat(1)},
        {"input": 2, "output": solution.nthPersonGetsNthSeat(2)},
        {"input": 10, "output": solution.nthPersonGetsNthSeat(10)},
        {"input": 100, "output": solution.nthPersonGetsNthSeat(100)},
        {"input": 1000, "output": solution.nthPersonGetsNthSeat(1000)},
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
    max_n = 1000
    test_cases = generate_test_cases(num_cases, max_n)
    save_test_cases("../test_cases_1227.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'nth_person_gets_nth_seat_test_cases.json'.")
