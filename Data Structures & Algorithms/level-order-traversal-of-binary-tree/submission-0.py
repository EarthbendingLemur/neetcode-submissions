# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        cur = root
        q.append([cur, 1])
        mp = defaultdict(list)
        max_level = 1
        while q:
            node, level = q.popleft()
            mp[level].append(node.val)
            max_level = max(level, max_level)
            if node and node.left:
                q.append([node.left, level + 1])
            if node and node.right:
                q.append([node.right, level + 1])
        
        res = [None] * max_level
        for k,v in mp.items():
            res[k - 1] = mp[k]

        return res