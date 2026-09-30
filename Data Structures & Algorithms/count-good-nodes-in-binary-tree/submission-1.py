# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        # Store in stack node, max seen so far
        stack = [(root, root.val)]
        while stack:
            node, maxSoFar = stack.pop()
            if node.val >= maxSoFar:
                res += 1
            maxSoFar = max(maxSoFar, node.val)

            if node.left:
                stack.append((node.left, maxSoFar))
            if node.right:
                stack.append((node.right, maxSoFar))
        
        return res





