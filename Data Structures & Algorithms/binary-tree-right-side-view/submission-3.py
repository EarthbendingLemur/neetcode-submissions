# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        levels = defaultdict(list)
        q.append((root, 1))
        res = []
        while q:
            node, level = q.popleft()
            if not node:
                break
            levels[level].append(node.val)
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))
        
        for k, v in levels.items():
            res.append(v[0])

        return res