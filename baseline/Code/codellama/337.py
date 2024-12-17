from typing import List
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            return [
                max(left[0], left[1]) + max(right[0], right[1]),
                node.val + left[0] + right[0],
            ]

        return max(dfs(root))