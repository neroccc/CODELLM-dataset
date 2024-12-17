from typing import List, Any, Optional
from deepseekcode.help.helphelp import TreeNode, deserialize_tree
class Solution:
    def rob(self, root: List[Any]) -> int:
        root: Optional[TreeNode] = deserialize_tree(root)
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        return max(dfs(root))