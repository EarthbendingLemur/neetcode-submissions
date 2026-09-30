# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS multisource with reversal each iteration

        res = []
        if not root:
            return []
        reverseFlag = False
    
        q = deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    continue
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverseFlag:
                res.append(level[::-1])
                reverseFlag = False
            else:
                res.append(level)
                reverseFlag = True
            
        

        return res
        

        

