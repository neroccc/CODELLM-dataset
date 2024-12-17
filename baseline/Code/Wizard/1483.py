from typing import List
class TreeAncestor:

    def __init__(self, n: int, parent: List[int]) -> None:
        self.parent = parent
        self.dp = [[0]*n for _ in range(20)]
        for i in range(n):
            self.dp[0][i] = parent[i]
        for i in range(1, 20):
            for j in range(n):
                if self.dp[i-1][j] != -1:
                    self.dp[i][j] = self.dp[i-1][self.dp[i-1][j]]
                else:
                    self.dp[i][j] = -1

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(19, -1, -1):
            if (k>>i)&1:
                node = self.dp[i][node]
                if node == -1:
                    return -1
        return node