# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        if not root:
            return 0

        q = deque([(root, 1)])

        while q:
            node, level = q.popleft()
            res = max(level, res)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        print()
        return res