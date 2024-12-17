from typing import List, Any
from deepseekcode.help.helphelp import TreeNode, deserialize_tree
class Solution:
    def minCameraCover(self, root: List[Any]) -> int:
        """
        Calculates the minimum number of cameras needed to monitor a binary tree provided in serialized format.
        :param serialized_tree: List representing the binary tree in level-order traversal.
        :return: Minimum number of cameras.
        """
        # Deserialize the tree from level-order format
        root = deserialize_tree(root)
        self.res = 0
        # 0: Strict st; 1: Normal st; 2: Pla
        def dfs(root: TreeNode) -> int:
            if not root:
                return 2
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0 or right == 0:
                self.res += 1
                return 1
            if left == 1 and right == 1:
                return 0
            if left == 2 and right == 2:
                return 2
            if left == 1 and right == 2 or left == 2 and right == 1:
                self.res += 1
                return 1
        if dfs(root) == 0:
            self.res += 1
        return self.res