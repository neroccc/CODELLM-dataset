from typing import List
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [-1, -1]
            left = dfs(node.left)
            right = dfs(node.right)
            self.ans = max(self.ans, left[0] + right[1] + 1)
            self.ans = max(self.ans, left[1] + right[0] + 1)
            return [max(left[0], right[1]) + 1, max(left[1], right[0]) + 1]

        self.ans = 0
        dfs(root)
        return self.ans