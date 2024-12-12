import json
import random
from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        res = [0] * n

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)

        return res


def generate_test_cases(num_cases=100):
    # Initialize the solution object
    solution = Solution()

    # Generate test cases
    test_cases = []
    for _ in range(num_cases):
        # Generate a random number of nodes between 1 and 10^3 for practicality
        n = random.randint(1, 1000)
        # Generate edges for a tree
        edges = []
        for i in range(1, n):
            edges.append([random.randint(0, i - 1), i])

        # Compute the output using the solution's method
        output = solution.sumOfDistancesInTree(n, edges)
        # Append the test case
        test_cases.append({
            "input": {
                "n": n,
                "edges": edges
            },
            "output": output
        })

    # Save to a JSON file
    with open("test_cases_.json834", "w") as file:
        json.dump(test_cases, file, indent=4)


# Generate the test cases
generate_test_cases(num_cases=100)
