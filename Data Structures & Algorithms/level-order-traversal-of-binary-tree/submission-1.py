# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)

        q = deque()
        cur = root
        q.append((cur, 1))
        while q:
            node, level = q.popleft()
            if not node:
                continue
            levels[level].append(node.val)
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        res = []

        for k, v in levels.items():
            res.append(v)
        
        return res