import json
import random

def countDigitOne(n: int) -> int:
    countr = 0
    i = 1
    while i <= n:
        divider = i * 10
        countr += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return countr

def generate_test_cases(num_cases=100, max_value=10**9):
    """
    Generates test cases for the countDigitOne function.

    :param num_cases: Number of test cases to generate.
    :param max_value: Maximum value for n.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []

    for _ in range(num_cases):
        # Generate a random number between 0 and max_value
        n = random.randint(0, max_value)

        # Calculate the expected output using the provided function
        expected_output = countDigitOne(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_233.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_value=10**5)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
