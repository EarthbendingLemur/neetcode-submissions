"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        q = deque()
        q.append(root)
        while q:
            nodes_explored = []
            for _ in range(len(q)):
                node = q.popleft()
                nodes_explored.append(node)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            for i in range(len(nodes_explored)):
                if i == len(nodes_explored) - 1:
                    continue
                
                nodes_explored[i].next = nodes_explored[i + 1]
        
        return root





        
        