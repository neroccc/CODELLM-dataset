import json
import random
import string
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_sub(word):
            index = -1
            for ch in word:
                index = s.find(ch, index + 1)
                if index == -1:
                    return False
            return True

        c = 0
        for word in words:
            if is_sub(word):
                c += 1

        return c


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string s of length between 1 and 50,000
        length_s = random.randint(1, 50000)
        s = ''.join(random.choices(string.ascii_lowercase, k=length_s))

        # Generate a random list of words with length between 1 and 5000
        num_words = random.randint(1, 5000)
        words = [
            ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 50)))
            for _ in range(num_words)
        ]

        # Compute the output using the solution's method
        output = solution.numMatchingSubseq(s, words)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s,
                "words": words
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_792.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
