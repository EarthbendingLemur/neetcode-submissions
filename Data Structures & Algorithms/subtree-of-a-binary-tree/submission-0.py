# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
            stack = [(s, t)]
            while stack:
                node_s, node_t = stack.pop()

                if not node_s and not node_t:
                    continue
                
                if not node_s or not node_t or node_s.val != node_t.val:
                    return False
                
                stack.append((node_s.left, node_t.left))
                stack.append((node_s.right, node_t.right))
            
            return True
    

        # Base Cases
        if not subRoot: return True
        if not root and subRoot: return False

        if sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    