import json
import random


def generate_test_cases(num_cases=100, max_length=10 ** 5):
    test_cases = []

    for _ in range(num_cases):
        # Randomize length of the string
        length = random.randint(1, max_length)

        # Generate a random binary string of the given length
        binary_string = ''.join(random.choice('01') for _ in range(length))

        # Create an entry
        test_case = {
            "input": binary_string,
            "output": calculate_expected(binary_string)
        }
        test_cases.append(test_case)

    # Save test cases to a file
    with open("test_cases926_.json", "w") as f:
        json.dump(test_cases, f, indent=2)


def calculate_expected(s):
    ones, ans = 0, 0
    for digit in s:
        if digit == '1':
            ones += 1
        elif ones:
            ones -= 1
            ans += 1
    return ans


# Generate test cases
generate_test_cases()
