# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        left, right = head, prev

        while left != second:
            tmp1 = left.next if left else None
            tmp2 = right.next if right else None
            
            if left:
                left.next = right 
            if right:
                right.next = tmp1 
            left = tmp1
            right = tmp2
        
