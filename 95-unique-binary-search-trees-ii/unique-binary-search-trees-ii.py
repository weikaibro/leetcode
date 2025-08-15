# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def recursive(start, end):
            if start > end:
                return [None]

            result = []
            for root in range(start, end + 1):
                left_tree = recursive(start, root - 1)
                right_tree = recursive(root + 1, end)
                for left_node in left_tree:
                    for right_node in right_tree:
                        node = TreeNode(root, left_node, right_node)
                        result.append(node)
            return result
        return recursive(1, n)