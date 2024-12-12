import json
import random
import string

# Provided solution
class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {text[i], "."}
                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

# Function to generate random strings
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

# Function to generate random patterns
def generate_random_pattern(length):
    pattern = []
    for _ in range(length):
        if random.random() < 0.2:  # 20% chance of adding '*'
            if pattern:  # Only add '*' if there is a preceding element
                pattern.append('*')
        elif random.random() < 0.3:  # 30% chance of adding '.'
            pattern.append('.')
        else:
            pattern.append(random.choice(string.ascii_lowercase))
    return ''.join(pattern)

# Generate test cases
def generate_test_cases(num_cases=1000):
    test_cases = []
    solver = Solution()

    for _ in range(num_cases):
        s_length = random.randint(1, 20)
        p_length = random.randint(1, 20)
        s = generate_random_string(s_length)
        p = generate_random_pattern(p_length)
        result = solver.isMatch(s, p)

        test_cases.append({"input": {"s": s, "p": p}, "output": result})

    return test_cases

# Save test cases to a JSON file
def save_test_cases_to_file(file_name, test_cases):
    with open(file_name, 'w') as f:
        json.dump(test_cases, f, indent=4)

if __name__ == "__main__":
    test_cases = generate_test_cases(1000)
    save_test_cases_to_file("../test_cases_10.json", test_cases)
