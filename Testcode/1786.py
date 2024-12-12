import json
import random
from collections import defaultdict, deque
from functools import lru_cache
from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        dist = {n: 0}
        queue = deque([n])
        while queue:
            u = queue.popleft()
            for v, w in graph[u]:
                if v not in dist or dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    queue.append(v)

        @lru_cache(None)
        def dfs(node):
            if node == n:
                return 1
            total_paths = 0
            for neighbor, _ in graph[node]:
                if dist[node] > dist[neighbor]:
                    total_paths += dfs(neighbor)
            return total_paths

        return dfs(1) % 1_000_000_007


# Helper function to generate random graphs
def generate_random_graph(n, max_edges, max_weight):
    edges = []
    seen = set()
    while len(edges) < max_edges:
        u, v = random.randint(1, n), random.randint(1, n)
        if u != v and (u, v) not in seen and (v, u) not in seen:
            weight = random.randint(1, max_weight)
            edges.append([u, v, weight])
            seen.add((u, v))
    return edges


# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(2, 1000)  # Generate a moderate-sized graph
        max_edges = random.randint(n - 1, min(4 * 10 ** 4, n * (n - 1) // 2))
        edges = generate_random_graph(n, max_edges, 10 ** 5)
        expected_output = solution.countRestrictedPaths(n, edges)

        test_cases.append({
            "input": {"n": n, "edges": edges},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1786.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
