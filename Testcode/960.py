import json
import random
import string
from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])

        isValid = lambda x: all(s[x] <= s[j] for s in strs)

        dp = [1] * n

        for j in range(1, n):
            dp[j] = max((dp[x] for x in filter(isValid, range(j))), default=0) + 1

        return n - max(dp)

def generate_random_strings(num_strings, string_length):
    """Generate a list of random strings."""
    return [''.join(random.choice(string.ascii_lowercase) for _ in range(string_length)) for _ in range(num_strings)]

def generate_test_cases(num_cases=50, max_strings=100, max_length=100):
    """Generate test cases for the Minimum Deletion Size problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        num_strings = random.randint(1, max_strings)
        string_length = random.randint(1, max_length)
        strs = generate_random_strings(num_strings, string_length)
        expected_output = solution.minDeletionSize(strs)
        test_cases.append({"input": strs, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": ["babca", "bbazb"], "output": solution.minDeletionSize(["babca", "bbazb"])},
        {"input": ["edcba"], "output": solution.minDeletionSize(["edcba"])},
        {"input": ["ghi", "def", "abc"], "output": solution.minDeletionSize(["ghi", "def", "abc"])},
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
    max_strings = 100
    max_length = 100
    test_cases = generate_test_cases(num_cases, max_strings, max_length)
    save_test_cases("test_cases_960.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'min_deletion_size_test_cases.json'.")
