# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(list)
        def BFS():
            q = deque()
            q.append((root, 0))
            while q:
                node, level = q.popleft()
                if not node:
                    continue
                levels[level].append(node)
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))

        BFS()
        res = [None] * len(levels)
        for level, nodes in levels.items():
            res[level] = levels[level][-1].val

        return res