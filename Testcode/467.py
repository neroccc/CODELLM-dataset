import json
import string
import random


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0

        count = {}
        curr_count = 0
        max_len = 1
        prev = s[0]

        for i in range(len(s)):
            if ord(s[i]) - ord(prev) == 1 or ord(prev) - ord(s[i]) == 25:
                max_len += 1
            else:
                max_len = 1

            if max_len >= curr_count:
                curr_count = max_len
            else:
                curr_count = 1

            count[s[i]] = max(count.get(s[i], 0), curr_count)

            prev = s[i]

        return sum(count.values())


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    # Helper to generate a random wraparound sequence
    def generate_wraparound_string(length):
        start = random.choice(string.ascii_lowercase)
        return ''.join(
            chr((ord(start) - ord('a') + i) % 26 + ord('a'))
            for i in range(length)
        )

    for _ in range(num_cases):
        # Generate random strings of varying lengths
        s_length = random.randint(1, 100)  # Adjust as needed for larger cases
        s = generate_wraparound_string(s_length)

        # Calculate expected output
        expected_output = solution.findSubstringInWraproundString(s)

        # Add test case
        test_cases.append({
            "input": {"s": s},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_467.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
