from typing import List, Any
from deepseekcode.help.helphelp import TreeNode, serialize_tree
class Solution:
    def generateTrees(self, n: int) -> List[List[Any]]:
        def generate(start, end):
            if start > end:
                return [None]
            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            return all_trees

        return generate(1, n) if n else []