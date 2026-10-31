from collections import defaultdict
from collections import deque
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        adj = defaultdict(list)
        root = None
        nodes = set()
        children = set()
        for p, c, isLeft in descriptions:
            nodes.add(p)
            nodes.add(c)
            children.add(c)
            adj[p].append((c, isLeft))
        
        for n in nodes:
            if n not in children:
                root = TreeNode(n)
                break
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            
            for c, isLeft in adj[node.val]:
                newNode = TreeNode(c)
                if isLeft:
                    node.left = newNode
                else:
                    node.right = newNode
                q.append(newNode)


        return root