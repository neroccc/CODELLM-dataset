import json
import random
from typing import List


class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)

        # If the total sum is not divisible by k, we can't make subsets.
        total_array_sum = sum(arr)
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        mask = 0

        memo = {}

        def backtrack(index, count, curr_sum):
            nonlocal mask
            n = len(arr)

            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True

            # No need to proceed further.
            if curr_sum > target_sum:
                return False

            # If we have already computed the current combination.
            if mask in memo:
                return memo[mask]

            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[mask] = backtrack(0, count + 1, 0)
                return memo[mask]

            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if ((mask >> j) & 1) == 0:
                    # Include this element in current subset.
                    mask = (mask | (1 << j))

                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True

                    # Backtrack step.
                    mask = (mask ^ (1 << j))

            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            memo[mask] = False
            return memo[mask]

        return backtrack(0, 0, 0)


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random array length between 1 and 16
        n = random.randint(1, 16)
        # Generate random values for the array elements between 1 and 10^4
        arr = [random.randint(1, 10 ** 4) for _ in range(n)]
        # Generate a random k within the range [1, n]
        k = random.randint(1, n)
        # Compute the output using the solution's method
        output = solution.canPartitionKSubsets(arr, k)
        # Append the test case
        test_cases.append({
            "input": {
                "nums": arr,
                "k": k
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_698.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=1000)
