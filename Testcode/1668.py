import json
import random
import string


class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0

        left = 1
        right = len(sequence) // len(word)
        while left <= right:
            mid = (left + right) // 2
            if word * mid in sequence:
                left = mid + 1
            else:
                right = mid - 1

        return left - 1


# Helper function to generate random strings
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        sequence_length = random.randint(1, 100)
        word_length = random.randint(1, min(100, sequence_length))
        sequence = generate_random_string(sequence_length)
        word = generate_random_string(word_length)

        expected_output = solution.maxRepeating(sequence, word)

        test_cases.append({
            "input": {"sequence": sequence, "word": word},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1668.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
