import json
import random

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (i + 1) for i in range(query_row + 1)]
        tower[0][0] = poured

        for row in range(query_row):
            for glass in range(len(tower[row])):
                excess = (tower[row][glass] - 1) / 2.0
                if excess > 0:
                    tower[row + 1][glass] += excess
                    tower[row + 1][glass + 1] += excess

        return min(1.0, tower[query_row][query_glass])


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random poured value between 0 and 10^9
        poured = random.randint(0, 10**9)
        # Generate random query_row and query_glass values
        query_row = random.randint(0, 99)
        query_glass = random.randint(0, query_row)
        # Compute the output using the solution's method
        output = solution.champagneTower(poured, query_row, query_glass)
        # Append the test case
        test_cases.append({
            "input": {
                "poured": poured,
                "query_row": query_row,
                "query_glass": query_glass
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_799.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
