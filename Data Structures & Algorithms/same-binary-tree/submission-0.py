# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        
        while stack:
            (node_P, node_Q) = stack.pop()

            if not node_P and not node_Q:
                continue
        
            if not node_P or not node_Q or node_P.val != node_Q.val:
                return False
            
            stack.append((node_P.right, node_Q.right))
            stack.append((node_P.left, node_Q.left))
    
        return True
        
