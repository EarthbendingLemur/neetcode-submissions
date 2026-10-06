# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        par = {root: None}

        stack = [root]
        while stack:
            node = stack.pop()

            if node.left:
                par[node.left] = node
                stack.append(node.left)
            
            if node.right:
                par[node.right] = node
                stack.append(node.right)

        p_parents = set()
        cur = p
        while cur:
            p_parents.add(cur)
            cur = par[cur]

        cur = q
        while cur:
            if cur in p_parents:
                return cur
            cur = par[cur]

    
        return TreeNode()
                