import json
import random
from typing import List

class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        sorted_indexes = sorted(range(len(A)), key=lambda i: A[i])
        oddnext = self.makeStack(sorted_indexes)
        sorted_indexes.sort(key=lambda i: A[i], reverse=True)
        evennext = self.makeStack(sorted_indexes)

        odd = [False] * len(A)
        even = [False] * len(A)

        odd[len(A) - 1] = even[len(A) - 1] = True

        for i in range(len(A) - 2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)

    def makeStack(self, sorted_indexes):
        result = [None] * len(sorted_indexes)
        stack = []
        for i in sorted_indexes:
            while stack and i > stack[-1]:
                result[stack.pop()] = i
            stack.append(i)
        del stack
        return result


def generate_random_array(max_length=20000, max_value=100000):
    """Generate a random array with length and values within specified limits."""
    length = random.randint(1, max_length)
    return [random.randint(0, max_value) for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=20000, max_value=100000):
    """Generate test cases for the Odd-Even Jumps problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        arr = generate_random_array(max_length, max_value)
        expected_output = solution.oddEvenJumps(arr)
        test_cases.append({"input": arr, "output": expected_output})

    # Add predefined edge cases
    predefined_cases = [
        {"input": [10, 13, 12, 14, 15], "output": solution.oddEvenJumps([10, 13, 12, 14, 15])},
        {"input": [2, 3, 1, 1, 4], "output": solution.oddEvenJumps([2, 3, 1, 1, 4])},
        {"input": [5, 1, 3, 4, 2], "output": solution.oddEvenJumps([5, 1, 3, 4, 2])},
        {"input": [1], "output": solution.oddEvenJumps([1])},
        {"input": [random.randint(0, 100000) for _ in range(20000)], "output": solution.oddEvenJumps([random.randint(0, 100000) for _ in range(20000)])},
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
    max_length = 20000
    max_value = 100000
    test_cases = generate_test_cases(num_cases, max_length, max_value)
    save_test_cases("test_cases_975.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'odd_even_jumps_test_cases.json'.")
