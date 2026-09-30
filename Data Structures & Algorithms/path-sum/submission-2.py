# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if not root:
            return False

        def dfs(root_node):
            stack = [(root_node, root_node.val)]

            while stack:
                node, sm = stack.pop()
                if sm == targetSum and not node.left and not node.right:
                    return True
                
                if node.left:
                    stack.append((node.left, sm + node.left.val))
                if node.right:
                    stack.append((node.right, sm + node.right.val))
            
        if dfs(root):
            return True
        return False

