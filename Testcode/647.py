import json
import random
import string


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        total = n

        center = 0.0
        while center < n:
            if center.is_integer():
                left, right = int(center) - 1, int(center) + 1
            else:
                left, right = int(center), int(center) + 1

            while left >= 0 and right < n:
                if s[left] != s[right]:
                    break
                total += 1
                left -= 1
                right += 1

            center += 0.5

        return total


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string of length between 1 and 1000
        length = random.randint(1, 1000)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        # Compute the output using the solution's method
        output = solution.countSubstrings(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_647.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
