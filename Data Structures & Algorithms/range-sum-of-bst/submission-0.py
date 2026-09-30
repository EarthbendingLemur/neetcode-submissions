# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        q = deque()
        sm = 0
        q.append(root)
        while q:
            node = q.popleft()
            if low <= node.val <= high:
                sm += node.val
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return sm

