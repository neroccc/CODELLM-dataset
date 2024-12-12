import json
import random
import string
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        len_s = len(s)
        dp = [[False] * len_s for _ in range(len_s)]
        result = []
        self.dfs(result, s, 0, [], dp)
        return result

    def dfs(
        self,
        result: List[List[str]],
        s: str,
        start: int,
        currentList: List[str],
        dp: List[List[bool]],
    ):
        if start >= len(s):
            result.append(list(currentList))
        for end in range(start, len(s)):
            if s[start] == s[end] and (
                end - start <= 2 or dp[start + 1][end - 1]
            ):
                dp[start][end] = True
                currentList.append(s[start : end + 1])
                self.dfs(result, s, end + 1, currentList, dp)
                currentList.pop()

def generate_random_string(length: int) -> str:
    """
    Generates a random lowercase English string.

    :param length: Length of the string to generate.
    :return: Random string of the specified length.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_test_cases(num_cases=100, max_length=16):
    """
    Generates test cases for the partition function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the input string.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the string
        length = random.randint(1, max_length)
        s = generate_random_string(length)

        # Calculate the expected output using the provided solution
        expected_output = solution.partition(s)

        # Add test case
        test_cases.append({
            "input": s,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_131.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=16)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
