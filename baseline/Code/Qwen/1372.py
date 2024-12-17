from typing import List, Any, Optional
from deepseekcode.help.helphelp import TreeNode, deserialize_tree
class Solution:
    def longestZigZag(self, root: List[Any]) -> int:
        root: Optional[TreeNode] = deserialize_tree(root)
        self.ans = 0

        def dfs(node: Optional[TreeNode], direction: str, length: int):
            if not node:
                return
            self.ans = max(self.ans, length)
            if direction == "left":
                dfs(node.right, "right", length + 1)
                dfs(node.left, "left", 1)
            else:
                dfs(node.left, "left", length + 1)
                dfs(node.right, "right", 1)

        dfs(root, "left", 0)
        dfs(root, "right", 0)
        return self.ans