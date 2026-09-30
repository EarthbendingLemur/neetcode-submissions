# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        left_h = self.height(root.left) if root.left else 0
        right_h = self.height(root.right) if root.right else 0

        if abs(left_h - right_h) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right) 
        


    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.height(root.right), self.height(root.left))