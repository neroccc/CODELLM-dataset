import json

MOD = 10 ** 9 + 7


class Solution:
    def countOrders(self, n: int) -> int:
        count = 1
        for i in range(2, n + 1):
            count = (count * (2 * i - 1) * i) % MOD
        return count


# Generate test cases
def generate_test_cases():
    solution = Solution()
    test_cases = []

    for n in range(1, 501):  # Constraints: 1 <= n <= 500
        # Compute the expected output using the solution
        expected_output = solution.countOrders(n)
        # Add the test case to the list
        test_cases.append({"input": n, "output": expected_output})

    # Save the test cases to a file
    with open("test_cases_1359.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases()
