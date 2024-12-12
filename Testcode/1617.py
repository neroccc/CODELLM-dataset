import json
import random
from collections import defaultdict


class Solution:
    def countSubgraphsForEachDiameter(self, n, edges):
        res = [0] * (n - 1)
        g = defaultdict(list)
        gs = [0] * n
        dp = [0] * (1 << n)
        for a, b in edges:
            a -= 1
            b -= 1
            g[a].append(b)
            g[b].append(a)
            gs[a] |= (1 << b)
            gs[b] |= (1 << a)
            dp[(1 << a) | (1 << b)] = 1
        dis = [[0] * n for _ in range(n)]

        def dfs(root, cur, depth, parent):
            dis[root][cur] = depth
            for nxt in g[cur]:
                if nxt == parent:
                    continue
                dfs(root, nxt, depth + 1, cur)

        for i in range(n):
            dfs(i, i, 0, -1)

        for state in range(1 << n):
            if dp[state] > 0:
                res[dp[state] - 1] += 1
                for i in range(n):
                    if dp[state | (1 << i)] == 0 and (state & gs[i]):
                        dp[state | (1 << i)] = max(dp[state], max(dis[i][j] for j in range(n) if state & (1 << j)))
        return res


# Helper function to generate a random tree
def generate_random_tree(n):
    edges = []
    for i in range(2, n + 1):
        edges.append([random.randint(1, i - 1), i])
    return edges


# Generate test cases
def generate_test_cases(num_cases=100):
    test_cases = []
    solution = Solution()

    for _ in range(num_cases):
        n = random.randint(2, 15)
        edges = generate_random_tree(n)
        expected_output = solution.countSubgraphsForEachDiameter(n, edges)

        test_cases.append({
            "input": {"n": n, "edges": edges},
            "output": expected_output
        })

    # Save to file
    with open("test_cases_1617.json", "w") as f:
        json.dump(test_cases, f, indent=4)


# Generate and save the test cases
generate_test_cases()
