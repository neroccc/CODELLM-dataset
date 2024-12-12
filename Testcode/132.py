import json
import random
import string
from typing import List

class Solution:
    def __init__(self):
        self.memoCuts = []
        self.memoPalindrome = []

    def minCut(self, s: str) -> int:
        self.memoCuts = [[None] * len(s) for _ in range(len(s))]
        self.memoPalindrome = [[None] * len(s) for _ in range(len(s))]
        return self.findMinimumCut(s, 0, len(s) - 1, len(s) - 1)

    def findMinimumCut(self, s, start, end, minimumCut):
        if start == end or self.isPalindrome(s, start, end):
            return 0
        if self.memoCuts[start][end] is not None:
            return self.memoCuts[start][end]
        for currentEndIndex in range(start, end + 1):
            if self.isPalindrome(s, start, currentEndIndex):
                minimumCut = min(
                    minimumCut,
                    1
                    + self.findMinimumCut(
                        s, currentEndIndex + 1, end, minimumCut
                    ),
                )
        self.memoCuts[start][end] = minimumCut
        return self.memoCuts[start][end]

    def isPalindrome(self, s, start, end):
        if start >= end:
            return True
        if self.memoPalindrome[start][end] is not None:
            return self.memoPalindrome[start][end]
        self.memoPalindrome[start][end] = (
            s[start] == s[end]
        ) and self.isPalindrome(s, start + 1, end - 1)
        return self.memoPalindrome[start][end]

def generate_random_string(length: int) -> str:
    """
    Generates a random lowercase English string.

    :param length: Length of the string to generate.
    :return: Random string of the specified length.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_test_cases(num_cases=100, max_length=2000):
    """
    Generates test cases for the minCut function.

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
        expected_output = solution.minCut(s)

        # Add test case
        test_cases.append({
            "input": s,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_132.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=20)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
