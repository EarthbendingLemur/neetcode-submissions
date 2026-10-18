# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        if not root:
            return None
        reverse = False
        while q:
            this_level = []
            for _ in range(len(q)):
                node = q.popleft()
                if reverse:
                    this_level.append(node)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverse:
                l, r = 0, len(this_level) - 1
                while l < r:
                    this_level[l].val, this_level[r].val = this_level[r].val, this_level[l].val
                    l += 1
                    r -= 1
    
            reverse = not reverse
        
        return root



