import json
import random
import string

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    )
        return dp[len(s2)]

def generate_test_cases(num_cases=1000, max_length=50):
    """
    Generates test cases for the isInterleave function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the strings.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Random lengths for s1 and s2
        len_s1 = random.randint(0, max_length)
        len_s2 = random.randint(0, max_length)

        # Generate random strings
        s1 = ''.join(random.choices(string.ascii_lowercase, k=len_s1))
        s2 = ''.join(random.choices(string.ascii_lowercase, k=len_s2))

        # Randomly decide to generate a valid or invalid interleaving
        if random.choice([True, False]):
            # Valid interleaving
            s3 = ''.join(random.sample(s1 + s2, len(s1 + s2)))
            expected_output = True
        else:
            # Invalid interleaving (randomize or change characters)
            s3 = ''.join(random.choices(string.ascii_lowercase, k=len(s1) + len(s2)))
            expected_output = solution.isInterleave(s1, s2, s3)

        # Add test case
        test_cases.append({
            "input": {"s1": s1, "s2": s2, "s3": s3},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_97.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=1000, max_length=50)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
