import json
import random
from typing import List
from math import log2

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n))  # Maximum power of 2 for jumps
        self.dp = [[-1] * m for _ in range(n)]
        for j in range(m):
            for i in range(n):
                if j == 0:
                    self.dp[i][0] = parent[i]
                elif self.dp[i][j - 1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node

# Helper function to generate a random tree
def generate_random_tree(n: int):
    parent = [-1]  # Root node
    for i in range(1, n):
        parent.append(random.randint(0, i - 1))
    return parent

# Generate test cases
def generate_test_cases(num_cases=10):
    test_cases = []
    for _ in range(num_cases):
        n = random.randint(1, 50000)
        parent = generate_random_tree(n)
        tree_ancestor = TreeAncestor(n, parent)

        # Generate random queries
        num_queries = random.randint(1, 50000)
        queries = []
        for _ in range(num_queries):
            node = random.randint(0, n - 1)
            k = random.randint(1, n)
            result = tree_ancestor.getKthAncestor(node, k)
            queries.append({"node": node, "k": k, "output": result})

        test_cases.append({
            "input": {"n": n, "parent": parent, "queries": queries},
        })

    # Save test cases to a file
    with open("test_cases_1483.json", "w") as f:
        json.dump(test_cases, f, indent=4)

# Generate and save the test cases
generate_test_cases()
