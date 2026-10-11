"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()

        cur = p
        while cur:
            visited.add(cur)
            cur = cur.parent
        
        cur = q
        while cur:
            if cur in visited:
                return cur
            cur = cur.parent
        
        return None
            