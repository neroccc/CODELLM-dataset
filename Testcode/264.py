import json

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [0] * n  # DP array to store ugly numbers
        ugly_numbers[0] = 1  # The first ugly number is 1

        # Three pointers for the multiples of 2, 3, and 5
        index_multiple_of_2, index_multiple_of_3, index_multiple_of_5 = 0, 0, 0
        next_multiple_of_2, next_multiple_of_3, next_multiple_of_5 = 2, 3, 5

        # Generate ugly numbers until we reach the nth one
        for i in range(1, n):
            # Find the next ugly number as the minimum of the next multiples
            next_ugly_number = min(
                [next_multiple_of_2, next_multiple_of_3, next_multiple_of_5]
            )
            ugly_numbers[i] = next_ugly_number

            # Update the corresponding pointer and next multiple
            if next_ugly_number == next_multiple_of_2:
                index_multiple_of_2 += 1
                next_multiple_of_2 = ugly_numbers[index_multiple_of_2] * 2
            if next_ugly_number == next_multiple_of_3:
                index_multiple_of_3 += 1
                next_multiple_of_3 = ugly_numbers[index_multiple_of_3] * 3
            if next_ugly_number == next_multiple_of_5:
                index_multiple_of_5 += 1
                next_multiple_of_5 = ugly_numbers[index_multiple_of_5] * 5

        return ugly_numbers[n - 1]  # Return the nth ugly number

def generate_test_cases(num_cases=100, max_n=1690):
    """
    Generates test cases for the nthUglyNumber function.

    :param num_cases: Number of test cases to generate.
    :param max_n: Maximum value for n.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for i in range(1, num_cases + 1):
        # Generate a random value of n between 1 and max_n
        n = i  # Sequential test cases for coverage
        # Calculate the expected output using the provided solution
        expected_output = solution.nthUglyNumber(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_264.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_n=1690)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
