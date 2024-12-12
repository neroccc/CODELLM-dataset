import json
import random
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0

        for _ in range(k + 1):
            temp = dp[:]
            for flight in flights:
                if dp[flight[0]] != float('inf'):
                    temp[flight[1]] = min(temp[flight[1]], dp[flight[0]] + flight[2])
            dp = temp

        return dp[dst] if dp[dst] != float('inf') else -1


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random number of cities between 2 and 100
        n = random.randint(2, 100)
        # Generate random number of flights up to n * (n - 1) / 2
        num_flights = random.randint(0, min(500, n * (n - 1) // 2))
        # Generate flights with random src, dst, and price
        flights = [[random.randint(0, n - 1), random.randint(0, n - 1), random.randint(1, 10000)] for _ in
                   range(num_flights)]
        # Remove invalid flights (fromi == toi) and duplicates
        flights = list({tuple(f) for f in flights if f[0] != f[1]})
        # Generate random src, dst, and k
        src = random.randint(0, n - 1)
        dst = random.randint(0, n - 1)
        while src == dst:
            dst = random.randint(0, n - 1)
        k = random.randint(0, n - 1)
        # Compute the output using the solution's method
        output = solution.findCheapestPrice(n, flights, src, dst, k)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n,
                "flights": flights,
                "src": src,
                "dst": dst,
                "k": k
            },
            "output": output
        })

    # Save to a JSON file
    with open("../test_cases_787.json", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
