from typing import List, Any, Optional
from deepseekcode.help.helphelp import TreeNode, deserialize_tree
class Solution:
    def minCameraCover(self, root: List[Any]) -> int:
        root: Optional[TreeNode] = deserialize_tree(root)

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if left == -1 or right == -1:
                self.ans += 1
                return 1
            if left == 1 or right == 1:
                return 0
            return -1

        self.ans = 0
        if dfs(root) == -1:
            self.ans += 1
        return self.ans