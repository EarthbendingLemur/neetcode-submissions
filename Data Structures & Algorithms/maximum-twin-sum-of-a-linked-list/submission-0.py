# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        cur = head

        while cur:
            vals.append(cur.val)
            cur = cur.next
        
        L, R = 0, len(vals) - 1
        res = 0
        while L < R:
            res = max(res, vals[L] + vals[R])
            R -= 1
            L += 1
        
        return res