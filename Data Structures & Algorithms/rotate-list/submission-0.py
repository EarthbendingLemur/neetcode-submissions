# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        cur, n  = head, 0
        while cur:
            n += 1
            cur = cur.next
        
        k = k % n
        arr = [-1] * n
        cur, idx = head, 0
        while cur:
            arr[(idx + k) % n] = cur.val
            cur = cur.next
            idx += 1
        
        dummy = ListNode()
        cur = dummy
        for i in range(len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next
        

        return dummy.next
