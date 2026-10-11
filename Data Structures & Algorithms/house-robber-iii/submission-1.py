# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        cache = {None: 0}

        def nest_rob(root):
            if root in cache:
                return cache[root]
            
            cache[root] = root.val
            if root.left:
                cache[root] += nest_rob(root.left.left) + nest_rob(root.left.right)
            if root.right:
                cache[root] += nest_rob(root.right.right) + nest_rob(root.right.left)
            
            sm_children = nest_rob(root.right) + nest_rob(root.left)
            cache[root] = max(cache[root], sm_children)
            return cache[root]
        
        return nest_rob(root)