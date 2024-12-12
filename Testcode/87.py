import json
import random
import string

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False for j in range(n)] for i in range(n)] for l in range(n + 1)]
        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]
        for length in range(2, n + 1):
            for i in range(n + 1 - length):
                for j in range(n + 1 - length):
                    for new_length in range(1, length):
                        dp1 = dp[new_length][i]
                        dp2 = dp[length - new_length][i + new_length]
                        dp[length][i][j] |= dp1[j] and dp2[j + new_length]
                        dp[length][i][j] |= dp1[j + length - new_length] and dp2[j]
        return dp[n][0][0]

def generate_scrambled_string(s):
    """
    Generates a scrambled version of the input string.
    """
    if len(s) <= 1:
        return s
    split_index = random.randint(1, len(s) - 1)
    left = generate_scrambled_string(s[:split_index])
    right = generate_scrambled_string(s[split_index:])
    if random.choice([True, False]):
        return left + right
    else:
        return right + left

def generate_test_cases(num_cases=1000, max_length=30):
    """
    Generates test cases for the isScramble function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the strings.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the string
        length = random.randint(1, max_length)

        # Generate a random string
        s1 = ''.join(random.choices(string.ascii_lowercase, k=length))

        # Generate a scrambled or non-scrambled version of s1
        if random.choice([True, False]):
            s2 = generate_scrambled_string(s1)
            expected_output = True
        else:
            # Generate a completely random string of the same length
            s2 = ''.join(random.choices(string.ascii_lowercase, k=length))
            expected_output = solution.isScramble(s1, s2)

        # Add test case
        test_cases.append({
            "input": {"s1": s1, "s2": s2},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_87.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    num_cases = 1000
    test_cases = generate_test_cases(num_cases=num_cases, max_length=30)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
