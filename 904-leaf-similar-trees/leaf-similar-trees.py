# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaves(root):
            if root is None:
                return []

            if root.left is None and root.right is None:
                return [root.val]

            return get_leaves(root.left) + get_leaves(root.right)

        return get_leaves(root1) == get_leaves(root2)          

