from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []

        def helper(n):
            if n == 1:
                return [TreeNode()]

            result = []
            for i in range(1, n, 2):
                left = helper(i)
                right = helper(n - i - 1)
                for l in left:
                    for r in right:
                        root = TreeNode(0, l, r)
                        result.append(root)

            return result

        return helper(n)