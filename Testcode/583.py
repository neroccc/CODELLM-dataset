import json
import random
import string

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word2, word1 = word1, word2

        m, n = len(word1), len(word2)
        prev = [0] * (m + 1)

        for i in range(n - 1, -1, -1):
            curr = [0] * (m + 1)
            for j in range(m - 1, -1, -1):
                if word1[j] == word2[i]:
                    curr[j] = 1 + prev[j + 1]
                else:
                    curr[j] = max(curr[j + 1], prev[j])
            prev = curr
        return m + n - 2 * prev[0]


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Randomly generate lengths for word1 and word2
        len_word1 = random.randint(1, 500)
        len_word2 = random.randint(1, 500)
        # Generate random strings of the respective lengths
        word1 = ''.join(random.choices(string.ascii_lowercase, k=len_word1))
        word2 = ''.join(random.choices(string.ascii_lowercase, k=len_word2))
        # Compute the output using the solution's method
        output = solution.minDistance(word1, word2)
        # Append the test case
        test_cases.append({
            "input": {
                "word1": word1,
                "word2": word2
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_583.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
