from typing import List
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.parent = parent
        self.table = [[] for _ in range(n)]
        for i in range(1, n):
            self.table[parent[i]].append(i)

    def getKthAncestor(self, node: int, k: int) -> int:
        for _ in range(k):
            node = self.table[node][0]
        return node
