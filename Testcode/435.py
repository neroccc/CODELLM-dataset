from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        # Initialize count of non-overlapping intervals
        prev_end = float('-inf')
        count = 0

        # Iterate through intervals
        for start, end in intervals:
            if start >= prev_end:
                # If the current interval doesn't overlap, move the pointer
                prev_end = end
            else:
                # Overlapping interval, increment the removal count
                count += 1

        return count

import json
import random

def generate_test_cases(num_cases=100, max_intervals=1000, value_range=(-50000, 50000)):
    """
    Generates test cases for the eraseOverlapIntervals function.

    :param num_cases: Number of test cases to generate.
    :param max_intervals: Maximum number of intervals in each test case.
    :param value_range: Range of values for interval start and end points.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        num_intervals = random.randint(1, max_intervals)
        intervals = []

        for _ in range(num_intervals):
            start = random.randint(*value_range)
            end = random.randint(start + 1, start + random.randint(1, 10))
            intervals.append([start, end])

        # Calculate the expected output using the provided solution
        expected_output = solution.eraseOverlapIntervals(intervals)

        # Add test case
        test_cases.append({
            "input": intervals,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_435.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_intervals=20, value_range=(-100, 100))

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
