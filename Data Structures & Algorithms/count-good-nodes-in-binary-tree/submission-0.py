# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 1

        def DFS(node_s):
            nonlocal res
            stack = [(node_s, node_s.val)]

            while stack:

                node, max_seen = stack.pop()

                if node.left:
                    if node.left.val >= max_seen:
                        res += 1
                    stack.append((node.left, max(node.left.val, max_seen)))
                if node.right:
                    if node.right.val >= max_seen:
                        res += 1
                    stack.append((node.right, max(node.right.val, max_seen)))
        
        DFS(root)

        return res