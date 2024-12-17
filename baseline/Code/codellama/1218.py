from typing import List
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            ans[0] = max(ans[0], left + right)
            return max(left, right)
        dfs(root)
        return ans[0]
