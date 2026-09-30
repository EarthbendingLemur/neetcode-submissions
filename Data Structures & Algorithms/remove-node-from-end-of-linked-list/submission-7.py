# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        prev = head
        tail = head
        
        for _ in range(n):
            tail = tail.next
        
        if tail is None:
            return head.next
        

        while tail and tail.next:
            prev = prev.next
            tail = tail.next
        
        prev.next = prev.next.next
        
        return head