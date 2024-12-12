import json
import random

class Solution:
    def maxScoreSightseeingPair(self, A):
        K = A[0]
        best = float('-inf')
        for j in range(1, len(A)):
            x = A[j]
            best = max(best, K + x - j)
            K = max(K, x + j)
        return best


def generate_random_values(max_length=50000, max_value=1000):
    """Generate a random array of values for sightseeing spots."""
    length = random.randint(2, max_length)
    return [random.randint(1, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=50000, max_value=1000):
    """Generate test cases for the Maximum Score of a Pair of Sightseeing Spots problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        values = generate_random_values(max_length, max_value)
        expected_output = solution.maxScoreSightseeingPair(values)
        test_cases.append({"input": values, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [8, 1, 5, 2, 6], "output": solution.maxScoreSightseeingPair([8, 1, 5, 2, 6])},
        {"input": [1, 2], "output": solution.maxScoreSightseeingPair([1, 2])},
        {"input": [1000] * 50000, "output": solution.maxScoreSightseeingPair([1000] * 50000)},
        {"input": [1, 1, 1, 1, 1], "output": solution.maxScoreSightseeingPair([1, 1, 1, 1, 1])},
        {"input": [1, 1000, 1, 1000, 1], "output": solution.maxScoreSightseeingPair([1, 1000, 1, 1000, 1])},
    ]
    test_cases.extend(predefined_cases)

    return test_cases


def save_test_cases(filename, test_cases):
    """Save test cases to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(test_cases, f, indent=4)


# Generate and save test cases
if __name__ == "__main__":
    num_cases = 100
    max_length = 50000
    max_value = 1000
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("../test_cases_1014.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'max_score_sightseeing_spots_test_cases.json'.")
