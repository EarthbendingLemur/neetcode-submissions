# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1, 2, 3, 4, 5] , n = 3
        #     ^     ^
        #     L     R
        
        L = head
        R = head
        for i in range(n):
            R = R.next
        
        if R is None:
            return head.next
        
        while R and R.next:
            R = R.next
            L = L.next
        
        L.next = L.next.next


        return head
