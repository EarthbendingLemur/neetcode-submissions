# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from collections import defaultdict
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        q = deque()
        # Keep track of total sum and parent
        q.append((root, root)) 
        while q:
            total_sum = 0
            par_mp = defaultdict(list)
            for _ in range(len(q)):
                node, parent = q.popleft()
                if parent:
                    par_mp[parent].append(node)
                total_sum += node.val
            
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            
            for _, children in par_mp.items():
                children_sum = 0
                for c in children:
                    children_sum += c.val
                
                for c in children:
                    c.val = total_sum - children_sum
        
        return root

