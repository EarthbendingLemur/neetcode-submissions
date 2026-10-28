# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        q = deque()
        q.append((root, 0))
        def checkLevel(this_level, full):
            if full:
                for n in this_level:
                    if n == -1:
                        return False
            
            foundNull = False
            for n in this_level:
                if foundNull and n == 1:
                    return False
                elif n == -1:
                    foundNull = True
            return True
        level = 0
        this_level = [1] * 2 ** level
        while q:
            if not checkLevel(this_level, True):
                return False
            this_level = [-1] * 2 ** level
            for _ in range(len(q)):
                node, i = q.popleft()
                this_level[i] = 1

                if node.left:
                    q.append((node.left, 2*i))                
                if node.right:
                    q.append((node.right, 2*i + 1))
            print(this_level)
            if not checkLevel(this_level, False):
                return False

            level += 1
        

        return True


