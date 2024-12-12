import json
import random
import string
from collections import defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
        The key ideas behind the solution:
        1. The maximum possible substrings that can end at an index are i + 1.
        2. The contribution of a character to this substring is (i + 1) - its last seen position.
        3. At each point, the sum of all contributions gives the number of total substrings found so far.
        4. The last seen position of char is actually i + 1.
        """
        last_position = defaultdict(int)  # Used for storing the last position of each character
        contribution = defaultdict(int)  # Used for storing the contribution of each character so far
        res = 0

        for i, char in enumerate(s):
            max_possible_substrs_at_idx = i + 1
            contribution[char] = max_possible_substrs_at_idx - last_position[char]

            res += sum(contribution.values())
            last_position[char] = i + 1

        return res


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string length between 1 and 10^5
        length = random.randint(1, 100)
        # Generate a random uppercase string of given length
        s = ''.join(random.choices(string.ascii_uppercase, k=length))
        # Compute the output using the solution's method
        output = solution.uniqueLetterString(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_828.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
