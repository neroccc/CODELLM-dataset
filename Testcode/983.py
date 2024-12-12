import json
import random
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1] + 1)]
        travel_days = set(days)
        for i in range(days[-1] + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 30)] + costs[2])
        return dp[-1]


def generate_random_days(max_days=365, max_length=365):
    """Generate a random array of travel days in strictly increasing order."""
    length = random.randint(1, max_length)
    days = sorted(random.sample(range(1, max_days + 1), length))
    return days


def generate_random_costs():
    """Generate a random array of ticket costs."""
    return [random.randint(1, 1000) for _ in range(3)]


def generate_test_cases(num_cases=50, max_days=365, max_length=365):
    """Generate test cases for the Minimum Cost For Tickets problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        days = generate_random_days(max_days, max_length)
        costs = generate_random_costs()
        expected_output = solution.mincostTickets(days, costs)
        test_cases.append({"input": {"days": days, "costs": costs}, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"days": [1, 4, 6, 7, 8, 20], "costs": [2, 7, 15]}, "output": solution.mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])},
        {"input": {"days": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], "costs": [2, 7, 15]}, "output": solution.mincostTickets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15])},
        {"input": {"days": [1], "costs": [10, 20, 30]}, "output": solution.mincostTickets([1], [10, 20, 30])},
        {"input": {"days": [1, 365], "costs": [2, 7, 15]}, "output": solution.mincostTickets([1, 365], [2, 7, 15])},
        {"input": {"days": list(range(1, 366)), "costs": [10, 50, 100]}, "output": solution.mincostTickets(list(range(1, 366)), [10, 50, 100])},
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
    save_test_cases("test_cases_983.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'min_cost_tickets_test_cases.json'.")
