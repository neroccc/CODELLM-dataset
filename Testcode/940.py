import json
import random
import string

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10 ** 9 + 7
        dp = [0] * 26  # dp[i] stores the counts of subsequences ending with letter i
        alphabet_indices = [ord(s[idx]) - 97 for idx in range(len(s) - 1, -1, -1)]
        for char in alphabet_indices:
            dp[char] = (1 + sum(dp)) % mod
        return sum(dp) % mod

def generate_random_string(length):
    """Generate a random string of given length."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_test_cases(num_cases=100, max_length=2000):
    """Generate test cases for the distinct subsequences problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, max_length)
        s = generate_random_string(length)
        expected_output = solution.distinctSubseqII(s)
        test_cases.append({"input": s, "output": expected_output})

    # Add some predefined edge cases
    predefined_cases = [
        {"input": "abc", "output": solution.distinctSubseqII("abc")},
        {"input": "aaa", "output": solution.distinctSubseqII("aaa")},
        {"input": "a" * max_length, "output": solution.distinctSubseqII("a" * max_length)},
        {"input": "abcdefghijklmnopqrstuvwxyz", "output": solution.distinctSubseqII("abcdefghijklmnopqrstuvwxyz")},
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
    max_length = 2000
    test_cases = generate_test_cases(num_cases, max_length)
    save_test_cases("test_cases_940.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'distinct_subsequences_test_cases.json'.")
