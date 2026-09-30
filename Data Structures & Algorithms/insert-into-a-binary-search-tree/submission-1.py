# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
         # Traverse until you find a leaf node 
         # Insert onto left or right of leaf node
        if not root:
            return TreeNode(val, None, None)
        def traverse(curr): 
            if not curr:
                return

            if not curr.left and curr.val > val:
                curr.left = TreeNode(val, None, None)
            
            if not curr.right and curr.val < val:
                curr.right = TreeNode(val, None, None)
            
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
            
            traverse(curr)
        
        traverse(root)
        return root
            
            

         