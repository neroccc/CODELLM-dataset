from collections import defaultdict
import bisect

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # no match at all, early exit

            # Greedy match with binary search
            indices_list = letter_indices_table[letter]
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False  # no suitable match found, early exit

        return True
import json
import random
import string

def generate_random_string(length: int) -> str:
    """
    Generates a random string of lowercase English letters.

    :param length: Length of the string.
    :return: Random string.
    """
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_test_cases(num_cases=100, max_s_length=100, max_t_length=10000):
    """
    Generates test cases for the isSubsequence function.

    :param num_cases: Number of test cases to generate.
    :param max_s_length: Maximum length of string s.
    :param max_t_length: Maximum length of string t.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        s_length = random.randint(0, max_s_length)
        t_length = random.randint(0, max_t_length)

        s = generate_random_string(s_length)
        t = generate_random_string(t_length)

        # Calculate the expected output using the provided solution
        expected_output = solution.isSubsequence(s, t)

        # Add test case
        test_cases.append({
            "input": {"s": s, "t": t},
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_392.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_s_length=100, max_t_length=1000)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
