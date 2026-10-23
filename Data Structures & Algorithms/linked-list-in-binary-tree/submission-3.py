class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        cur = head


        def traverse(root, pathing, cur):

            if not root:
                return False

            if pathing and root.val != cur.val:
                return False

            if root.val == cur.val:
                cur = cur.next
                if not cur:
                    return True
                pathing = True

            
            return traverse(root.left, pathing, cur) or traverse(root.right, pathing, cur)

        return traverse(root, False, cur)
            


