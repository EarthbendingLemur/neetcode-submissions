# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []

        if not root:
            return ""
        
        stack = [root]

        while stack:
            node = stack.pop()

            # Append all parentheses
            if isinstance(node, str):
                res.append(node)
                continue
            
            res.append(str(node.val))

            if node.right:
                stack.append(")")
                stack.append(node.right)
                stack.append("(")
            
            if node.left:
                stack.append(")")
                stack.append(node.left)
                stack.append("(")
            elif node.right:
                res.append("()")


        return "".join(res)


