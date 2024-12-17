from typing import List, Optional,Any


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: List[Any]) -> int:
        def deserialize_tree(data: List[Any]) -> Optional[TreeNode]:
            if not data:
                return None

            root = TreeNode(data[0])
            queue = [root]
            index = 1

            while queue and index < len(data):
                node = queue.pop(0)

                if data[index] is not None:
                    node.left = TreeNode(data[index])
                    queue.append(node.left)
                index += 1

                if index < len(data) and data[index] is not None:
                    node.right = TreeNode(data[index])
                    queue.append(node.right)
                index += 1

            return root

        root = deserialize_tree(root)
        def dfs(node):
            if not node:
                return 0, 1
            
            left_unmonitored, left_covered = dfs(node.left)
            right_unmonitored, right_covered = dfs(node.right)
            
            unmonitored = left_unmonitored + right_unmonitored
            covered = 0
            
            if left_unmonitored == 1 or right_unmonitored == 1:
                covered = 1
                unmonitored -= 1
            
            if left_covered == 0 or right_covered == 0:
                unmonitored += 1
            
            return unmonitored, covered
        
        return max(dfs(root))