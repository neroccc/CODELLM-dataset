import json

# Provided solution
class Solution:
    def generateParenthesis(self, n: int):
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res

# Generate test cases
def generate_test_cases(max_n=8):
    test_cases = []
    solver = Solution()

    for n in range(1, max_n + 1):
        result = solver.generateParenthesis(n)
        test_cases.append({"input": {"n": n}, "output": result})

    return test_cases

# Save test cases to a JSON file
def save_test_cases_to_file(file_name, test_cases):
    with open(file_name, 'w') as f:
        json.dump(test_cases, f, indent=4)

if __name__ == "__main__":
    test_cases = generate_test_cases(8)
    save_test_cases_to_file("../test_cases_22.json", test_cases)
