import json
import random
from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        f = [0] * (n + 1)

        for i, (w, h) in enumerate(books, 1):
            f[i] = f[i - 1] + h
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                if w > shelfWidth:
                    break
                h = max(h, books[j - 1][1])
                f[i] = min(f[i], f[j - 1] + h)

        return f[n]


def generate_random_books(min_length=1, max_length=1000, max_thickness=1000, max_height=1000):
    """Generate a random list of books with thickness and height."""
    length = random.randint(min_length, max_length)
    return [[random.randint(1, max_thickness), random.randint(1, max_height)] for _ in range(length)]


def generate_test_cases(num_cases=50, max_length=1000, max_thickness=1000, max_height=1000):
    """Generate test cases for the Minimum Height by Shelves problem."""
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        books = generate_random_books(1, max_length, max_thickness, max_height)
        shelfWidth = random.randint(max(1, max_thickness // 2), max_thickness)
        expected_output = solution.minHeightShelves(books, shelfWidth)
        test_cases.append({
            "input": {"books": books, "shelfWidth": shelfWidth},
            "output": expected_output
        })

    # Add predefined edge cases
    predefined_cases = [
        {"input": {"books": [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], "shelfWidth": 4},
         "output": solution.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4)},
        {"input": {"books": [[1, 3], [2, 4], [3, 2]], "shelfWidth": 6},
         "output": solution.minHeightShelves([[1, 3], [2, 4], [3, 2]], 6)},
        {"input": {"books": [[1, 1]], "shelfWidth": 1},
         "output": solution.minHeightShelves([[1, 1]], 1)},
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
    max_length = 1000
    max_thickness = 1000
    max_height = 1000
    test_cases = generate_test_cases(num_cases, max_length, max_thickness, max_height)
    save_test_cases("../test_cases_1105.json", test_cases)
    print(f"Generated {num_cases} test cases and saved to 'min_height_shelves_test_cases.json'.")
