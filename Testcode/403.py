class Solution:
    def canCross(self, stones):
        n = len(stones)
        stoneSet = set(stones)
        visited = set()

        def goFurther(value, units):
            if (value + units not in stoneSet) or ((value, units) in visited):
                return False
            if value + units == stones[n - 1]:
                return True
            visited.add((value, units))
            return (
                goFurther(value + units, units)
                or goFurther(value + units, units - 1)
                or goFurther(value + units, units + 1)
            )

        return goFurther(stones[0], 1)
import json
import random

def generate_stones(length, max_gap=10):
    """
    Generates a sorted list of stone positions.

    :param length: Number of stones.
    :param max_gap: Maximum gap between consecutive stones.
    :return: Sorted list of stone positions.
    """
    stones = [0]
    for _ in range(length - 1):
        stones.append(stones[-1] + random.randint(1, max_gap))
    return stones

def generate_test_cases(num_cases=100, max_stones=20, max_gap=10):
    """
    Generates test cases for the canCross function.

    :param num_cases: Number of test cases to generate.
    :param max_stones: Maximum number of stones.
    :param max_gap: Maximum gap between consecutive stones.
    :return: List of test cases with inputs and expected outputs.
    """
    solution = Solution()
    test_cases = []

    for _ in range(num_cases):
        stones = generate_stones(random.randint(2, max_stones), max_gap)

        # Calculate the expected output using the provided solution
        expected_output = solution.canCross(stones)

        # Add test case
        test_cases.append({
            "input": stones,
            "output": expected_output
        })

    return test_cases

def save_test_cases_to_file(test_cases, filename="test_cases_403.json"):
    """
    Saves test cases to a JSON file.

    :param test_cases: List of test cases to save.
    :param filename: Name of the file to save the test cases in.
    """
    with open(filename, "w") as file:
        json.dump(test_cases, file, indent=4)

if __name__ == "__main__":
    # Generate test cases
    test_cases = generate_test_cases(num_cases=100, max_stones=50, max_gap=15)

    # Save to file
    save_test_cases_to_file(test_cases)
    print("Test cases saved to 'test_case_.json'.")
