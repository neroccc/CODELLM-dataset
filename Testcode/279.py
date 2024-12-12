import json


class Solution:
    def numSquares(self, n: int) -> int:
        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            next_queue = set()
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level


def generate_test_cases(num_cases=100, max_n=10 ** 4):
    """
    Generates test cases for the numSquares function.

    :param num_cases: Number of test cases to generate.
    :param max_n: Maximum value for n.
    :return: List of test cases with inputs and expected outputs.
    """
    test_cases = []
    solution = Solution()

    for i in range(1, num_cases + 1):
        # Generate a random value of n between 1 and max_n
        n = i  # Sequential test cases for comprehensive coverage
        # Calculate the expected output using the provided solution
        expected_output = solution.numSquares(n)

        # Add test case
        test_cases.append({
            "input": n,
            "output": expected_output
        })

    return test_cases


def save_test_cases_to_file(test_cases, filename="test_cases_279.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)


if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_n=10 ** 4)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
