import json
import random

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random string of length between 1 and 100
        length = random.randint(1, 100)
        s = ''.join(random.choices("()*", k=length))
        # Compute the output using the solution's method
        output = solution.checkValidString(s)
        # Append the test case
        test_cases.append({
            "input": {
                "s": s
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_678.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
