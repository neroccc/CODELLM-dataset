import json
import random

class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for _ in range(N + 1)]
        for i in range(N + 1):
            for j in range(1, i // 2 + 1):
                if i % j == 0 and (not dp[i - j]):
                    dp[i] = True
                    break
        return dp[N]


def generate_test_cases(num_cases=50, max_n=1000):
    """Generate test cases for the Divisor Game problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(1, max_n)
        expected_output = solution.divisorGame(n)
        test_cases.append({"input": n, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": 1, "output": solution.divisorGame(1)},
        {"input": 2, "output": solution.divisorGame(2)},
        {"input": 3, "output": solution.divisorGame(3)},
        {"input": 1000, "output": solution.divisorGame(1000)},
        {"input": 10, "output": solution.divisorGame(10)},
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
    save_test_cases("../test_cases_1025.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'divisor_game_test_cases.json'.")
