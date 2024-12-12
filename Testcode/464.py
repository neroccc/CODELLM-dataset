import json
from itertools import combinations

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
            return False
        self.memo = {}
        return self.can_win(tuple(range(1, maxChoosableInteger+1)), desiredTotal)

    def can_win(self, choices, target):
        if choices[-1] >= target:
            return True
        if choices in self.memo:
            return self.memo[choices]
        for i in range(len(choices)):
            if not self.can_win(choices[:i]+choices[i+1:], target-choices[i]):
                self.memo[choices] = True
                return True
        self.memo[choices] = False
        return False

def generate_test_cases(solution, num_cases=100):
    test_cases = []
    for maxChoosableInteger in range(1, 21):  # Covers the range 1 <= maxChoosableInteger <= 20
        for desiredTotal in range(0, 301):   # Covers the range 0 <= desiredTotal <= 300
            test_case = {
                "maxChoosableInteger": maxChoosableInteger,
                "desiredTotal": desiredTotal
            }
            expected_output = solution.canIWin(maxChoosableInteger, desiredTotal)
            test_cases.append({
                "input": test_case,
                "output": expected_output
            })
            if len(test_cases) >= num_cases:  # Limit the number of test cases
                break
        if len(test_cases) >= num_cases:
            break
    return test_cases

# Instantiate the solution and generate test cases
solution = Solution()
test_cases = generate_test_cases(solution, num_cases=1000)

# Save the test cases to a JSON file
file_path = "../test_cases_464.json"
with open(file_path, "w") as file:
    json.dump(test_cases, file, indent=2)

print(f"Test cases have been saved to {file_path}.")
