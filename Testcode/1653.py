import json
import random

class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = count = 0
        for c in s:
            if c == 'b':
                count += 1
            elif count:
                res += 1
                count -= 1
        return res

# Helper function to generate random strings
def generate_random_string(length):
    return ''.join(random.choice(['a', 'b']) for _ in range(length))

# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        length = random.randint(1, 10**5)
        s = generate_random_string(length)
        expected_output = solution.minimumDeletions(s)

        test_cases.append({
            "input": {"s": s},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1653.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
