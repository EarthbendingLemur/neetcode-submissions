# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    delim = "-"
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return res
        
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            res += str(node.val) + ":"
            if node.left:
                q.append(node.left)
                res += str(node.left.val) + ","
            else:
                res += "N,"
            if node.right:
                q.append(node.right)
                res += str(node.right.val)
            else:
                res += "N"
            res += self.delim
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        levels = data.split(self.delim)
        
        root_val, children = levels[0].split(":")
        root = TreeNode(int(root_val))

        q = deque()
        q.append(root)
        i = 0
        while q: 
            par = q.popleft()       
        
            children = levels[i].split(":")[1]
            left, right = children.split(",")
            if left != "N":
                par.left = TreeNode(int(left))
                q.append(par.left)
            if right != "N":
                par.right = TreeNode(int(right))
                q.append(par.right)
            
            i += 1

            
        return root
