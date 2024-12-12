import json
import random
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Initialize memoization dictionary to store results of subproblems
        memo = {}
        # Solve for the entire expression
        return self._compute_results(expression, memo, 0, len(expression) - 1)

    def _compute_results(
        self, expression: str, memo: dict, start: int, end: int
    ) -> List[int]:
        # If result is already memoized, return it
        if (start, end) in memo:
            return memo[(start, end)]

        results = []

        # Base case: single digit
        if start == end:
            results.append(int(expression[start]))
            return results

        # Base case: two-digit number
        if end - start == 1 and expression[start].isdigit():
            results.append(int(expression[start : end + 1]))
            return results

        # Recursive case: split the expression at each operator
        for i in range(start, end + 1):
            if expression[i].isdigit():
                continue

            left_results = self._compute_results(expression, memo, start, i - 1)
            right_results = self._compute_results(expression, memo, i + 1, end)

            # Combine results from left and right subexpressions
            for left_value in left_results:
                for right_value in right_results:
                    if expression[i] == "+":
                        results.append(left_value + right_value)
                    elif expression[i] == "-":
                        results.append(left_value - right_value)
                    elif expression[i] == "*":
                        results.append(left_value * right_value)

        # Memoize the result for this subproblem
        memo[(start, end)] = results

        return results

def generate_random_expression(length: int) -> str:
    """
    Generates a random mathematical expression with digits and operators.

    :param length: Length of the expression (including operators).
    :return: Random mathematical expression as a string.
    """
    operators = ["+", "-", "*"]
    expression = str(random.randint(0, 9))
    for _ in range(length - 1):
        expression += random.choice(operators) + str(random.randint(0, 9))
    return expression

def generate_test_cases(num_cases=100, max_length=10):
    """
    Generates test cases for the diffWaysToCompute function.

    :param num_cases: Number of test cases to generate.
    :param max_length: Maximum length of the expressions.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        # Randomize the length of the expression
        length = random.randint(1, max_length)
        expression = generate_random_expression(length)

        # Calculate the expected output using the provided solution
        expected_output = solution.diffWaysToCompute(expression)

        # Add test case
        test_cases.append({
            "input": expression,
            "output": sorted(expected_output)
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_241.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_length=10)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
