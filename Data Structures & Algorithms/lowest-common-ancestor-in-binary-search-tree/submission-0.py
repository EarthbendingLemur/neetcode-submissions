# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        curr = root

        def traverse(curr):
            if not curr:
                return
            
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
                return traverse(curr)
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                return traverse(curr)
            
            if curr.val == p.val:
                return p
            if curr.val == q.val:
                return q
            
            return curr
        
        return traverse(curr)