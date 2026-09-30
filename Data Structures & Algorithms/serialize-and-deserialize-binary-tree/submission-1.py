# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    delimiter = "-"
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            
            serialised = str(node.val) + ":"
            if node.left:
                serialised += str(node.left.val) + ","
                q.append(node.left)
            else:
                serialised += "N" + ","
            if node.right:
                serialised += str(node.right.val) + ","
                q.append(node.right)
            else:
                serialised += "N" + ","
            serialised = serialised[:-1] + self.delimiter
            res += serialised
        return res

    def deserialize(self, data: str) -> Optional[TreeNode]:

        if not data:
            return None
        
        parts = data.split(self.delimiter)
        root_val, children = parts[0].split(":")
        root = TreeNode(int(root_val))

        q = deque()
        q.append(root)

        i = 0
        while q:
            parent = q.popleft()

            children = parts[i].split(":")[1]
            left_val, right_val = children.split(",")
        
            if left_val != "N":
                parent.left = TreeNode(int(left_val))
                q.append(parent.left)
            if right_val != "N":
                parent.right = TreeNode(int(right_val))
                q.append(parent.right)
            i += 1
        
        return root



        
