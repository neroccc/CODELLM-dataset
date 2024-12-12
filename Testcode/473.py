import json
import random
from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4 != 0 or max(matchsticks) > total_length // 4:
            return False
        target_length = total_length // 4
        matchsticks.sort(reverse=True)

        def form_sides(i, sides):
            if i == len(matchsticks) and all(side == target_length for side in sides):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= target_length:
                    new_sides = list(sides)
                    new_sides[j] += matchsticks[i]
                    if form_sides(i + 1, tuple(new_sides)):
                        return True

            return False

        return form_sides(0, (0, 0, 0, 0))


def generate_test_cases(solution, num_cases=100):
    test_cases = []

    for _ in range(num_cases):
        # Generate a random number of matchsticks
        num_matchsticks = random.randint(4, 15)

        # Generate matchstick lengths
        matchsticks = [random.randint(1, 20) for _ in range(num_matchsticks)]

        # Ensure some cases are solvable
        if random.random() < 0.5:
            # Generate a solvable case
            side_length = random.randint(1, 20)
            num_sides = 4
            matchsticks = []
            for _ in range(num_sides):
                matchsticks.extend([side_length] * (random.randint(1, 3)))
            random.shuffle(matchsticks)

        # Compute expected output using the provided solution
        expected_output = solution.makesquare(matchsticks)

        # Add test case
        test_cases.append({
            "input": {"matchsticks": matchsticks},
            "output": expected_output
        })

    return test_cases


# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_473.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
