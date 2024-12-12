import json
import random
import string


class Solution:
    def numSplits(self, s: str) -> int:
        left_count, right_count = {}, {}
        left_unique, right_unique = [0] * len(s), [0] * len(s)
        count_left, count_right = 0, 0

        for i, c in enumerate(s):
            if c not in left_count:
                count_left += 1
            left_count[c] = left_count.get(c, 0) + 1
            left_unique[i] = count_left

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c not in right_count:
                count_right += 1
            right_count[c] = right_count.get(c, 0) + 1
            right_unique[i] = count_right

        return sum(1 for i in range(len(s) - 1) if left_unique[i] == right_unique[i + 1])


# Helper function to generate random strings
def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10 ** 5)
        s = generate_random_string(length)

        # Compute expected output using the provided solution
        expected_output = solution.numSplits(s)

        test_cases.append({
            "input": {"s": s},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1525.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
