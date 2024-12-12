import json
import random
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        from math import inf
        from functools import cache

        graph = {}
        for u, v, time in roads:
            graph.setdefault(u, {})[v] = time
            graph.setdefault(v, {})[u] = time

        dist = [inf] * n
        dist[-1] = 0
        stack = [(n - 1, 0)]
        while stack:
            x, t = stack.pop()
            if t == dist[x]:
                for xx in graph.get(x, {}):
                    if t + graph[x][xx] < dist[xx]:
                        dist[xx] = t + graph[x][xx]
                        stack.append((xx, t + graph[x][xx]))

        @cache
        def fn(x):
            """Return the number of ways to reach destination."""
            if x == n - 1:
                return 1
            if dist[x] == inf:
                return 0
            ans = 0
            for xx in graph.get(x, {}):
                if graph[x][xx] + dist[xx] == dist[x]:
                    ans += fn(xx)
            return ans % 1_000_000_007

        return fn(0)


def generate_test_cases(num_cases=100, max_n=200):
    """Generate random test cases for the problem."""
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(2, max_n)  # Number of intersections
        m = random.randint(n - 1, n * (n - 1) // 2)  # Number of roads
        roads = []
        for _ in range(m):
            u = random.randint(0, n - 1)
            v = random.randint(0, n - 1)
            while u == v:  # Ensure no self-loops
                v = random.randint(0, n - 1)
            time = random.randint(1, 10 ** 9)  # Random travel time
            roads.append([u, v, time])
        test_cases.append({"n": n, "roads": roads})
    return test_cases


def compute_expected_outputs(test_cases):
    """Compute the expected outputs for the given test cases."""
    solution = Solution()
    outputs = []
    for case in test_cases:
        n = case["n"]
        roads = case["roads"]
        output = solution.countPaths(n, roads)
        outputs.append(output)
    return outputs


# Generate test cases
test_cases = generate_test_cases(num_cases=50, max_n=50)

# Compute expected outputs
expected_outputs = compute_expected_outputs(test_cases)

# Save test cases and outputs to a JSON file
test_data = [{"input": case, "output": output} for case, output in zip(test_cases, expected_outputs)]

with open("test_cases_1976.json", "w") as f:
    json.dump(test_data, f, indent=4)

print("Test cases generated and saved to 'test_case_.json'")
