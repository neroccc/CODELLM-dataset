import json

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        # Initialize the cache to store sub-problem results.
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Recursive function to return the count of combinations
        # of length 'n' eligible for the award.
        def eligible_combinations(n, total_absences, consecutive_lates):
            # If the combination has become not eligible for the award,
            # then we will not count any combinations that can be made using it.
            if total_absences >= 2 or consecutive_lates >= 3:
                return 0
            # If we have generated a combination of length 'n' we will count it.
            if n == 0:
                return 1
            # If we have already seen this sub-problem earlier,
            # we return the stored result.
            if memo[n][total_absences][consecutive_lates] != -1:
                return memo[n][total_absences][consecutive_lates]

            # We choose 'P' for the current position.
            count = eligible_combinations(n - 1, total_absences, 0)
            # We choose 'A' for the current position.
            count = (
                count + eligible_combinations(n - 1, total_absences + 1, 0)
            ) % MOD
            # We choose 'L' for the current position.
            count = (
                count
                + eligible_combinations(
                    n - 1, total_absences, consecutive_lates + 1
                )
            ) % MOD

            # Return and store the current sub-problem result in the cache.
            memo[n][total_absences][consecutive_lates] = count
            return count

        # Return count of combinations of length 'n' eligible for the award.
        return eligible_combinations(n, 0, 0)


def generate_test_cases(num_cases=1000, max_length=10**5):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for i in range(num_cases):
        n = i + 1  # Length of the attendance record (from 1 to num_cases)
        if n > max_length:
            break
        # Compute the output using the solution's method
        output = solution.checkRecord(n)
        test_cases.append({"input": {"n": n}, "output": output})

    # Save to a JSON file
    with open("../test_cases_552.json", "w") as file:
        json.dump(test_cases, file, indent=4)

# Generate the test cases
generate_test_cases(num_cases=100, max_length=1000)
