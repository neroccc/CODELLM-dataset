import json
import random


# Provided solution
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        max_length = 0

        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2
                max_length = max(max_length, dp[i])

        return max_length


# Function to generate random strings of parentheses
def generate_random_parentheses_string(length):
    return ''.join(random.choice(['(', ')']) for _ in range(length))


# Generate test cases
def generate_test_cases(num_cases=1000, max_length=100):
    test_cases = []
    solver = Solution()

    for _ in range(num_cases):
        length = random.randint(0, max_length)  # Random length between 0 and max_length
        s = generate_random_parentheses_string(length)
        result = solver.longestValidParentheses(s)

        test_cases.append({"input": {"s": s}, "output": result})

    return test_cases


# Save test cases to a JSON file
def save_test_cases_to_file(file_name, test_cases):
    with open(file_name, 'w') as f:
        json.dump(test_cases, f, indent=4)


if __name__ == "__main__":
    test_cases = generate_test_cases(num_cases=1000, max_length=100)
    save_test_cases_to_file("../test_cases_32.json", test_cases)
