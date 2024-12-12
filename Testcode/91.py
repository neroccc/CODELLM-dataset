import json
import random
from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        two_back = 1
        one_back = 1
        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current = one_back
            two_digit = int(s[i - 1 : i + 1])
            if 10 <= two_digit <= 26:
                current += two_back
            two_back = one_back
            one_back = current

        return one_back

def generate_test_cases(num_cases=1000, max_length=100):
    """
    Generates test cases for the numDecodings function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the strings.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the string
        length = random.randint(1, max_length)

        # Generate a random string of digits
        s = ''.join(random.choices('0123456789', k=length))

        # Ensure the string starts with a non-zero digit
        if s[0] == '0':
            s = str(random.randint(1, 9)) + s[1:]

        # Calculate the expected output using the provided solution
        expected_output = solution.numDecodings(s)

        # Add test case
        test_cases.append({
            "input": s,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_91.json"):
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
    test_cases = generate_test_cases(num_cases=num_cases, max_length=100)

    # Save to file
    save_test_cases_to_file(test_cases)
    print(f"{num_cases} test cases saved to 'test_case_.json'.")
