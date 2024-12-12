import json
import random
import math
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        n = len(passingFees)

        # adjacency list
        adj = [[] for _ in range(n)]
        for u, v, dt in edges:
            if dt > maxTime: continue
            adj[u].append((v, dt))
            adj[v].append((u, dt))

        # modified Dijkstra
        times = [math.inf] * n
        costs = [math.inf] * n
        times[0] = 0
        costs[0] = passingFees[0]
        pq = [(costs[0], times[0], 0)]  # explore by cost asc | time <= maxTime
        while pq:
            c, t, u = heappop(pq)

            if u == n - 1:
                return c  # first encounter of n-1 ordered by cost: min cost found

            if c > costs[u] and t > times[u]:
                continue  # stale entry in heap

            for v, dt in adj[u]:
                vt = t + dt
                vc = c + passingFees[v]

                if vt > maxTime:
                    continue  # illegal path

                if vc < costs[v]:
                    # new lowest cost, explore paths from here
                    costs[v] = vc
                    heappush(pq, (vc, vt, v))
                elif vt < times[v]:
                    # higher cost but less time, worth exploring
                    times[v] = vt
                    heappush(pq, (vc, vt, v))

        return -1  # no path to n-1 within maxTime


def generate_test_cases(num_cases=100, max_n=100, max_edges=100, max_time=1000, max_fee=1000):
    """Generate test cases for the minCost problem."""
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(2, max_n)  # Number of cities
        m = random.randint(n - 1, max_edges)  # Number of edges (at least n-1 to ensure connectivity)
        max_t = random.randint(1, max_time)  # Maximum time allowed
        passing_fees = [random.randint(1, max_fee) for _ in range(n)]

        # Generate random edges
        edges = []
        for _ in range(m):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            while u == v:  # Ensure no self-loops
                v = random.randint(0, n - 1)
            time = random.randint(1, max_time)
            edges.append([u, v, time])

        test_cases.append({"maxTime": max_t, "edges": edges, "passingFees": passing_fees})
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the given test cases."""
    solution = Solution()
    outputs = []
    for case in test_cases:
        maxTime = case["maxTime"]
        edges = case["edges"]
        passingFees = case["passingFees"]
        output = solution.minCost(maxTime, edges, passingFees)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=100, max_n=10, max_edges=20, max_time=100, max_fee=100)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": case, "output": output} for case, output in zip(test_cases, expected_outputs)]

with open("test_cases_1928.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
