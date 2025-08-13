# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs: level traversal
        if not root:
            return []
        d = deque([root])
        result = []
        while d:
            level_node_count = len(d)
            for i in range(len(d)):
                node = d.popleft()
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
                if i == level_node_count - 1:
                    result.append(node.val)
        return result