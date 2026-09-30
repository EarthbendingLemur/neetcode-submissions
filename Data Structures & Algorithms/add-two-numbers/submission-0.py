# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val_1 = val_2 = 0
            if l1:val_1 = l1.val
            if l2: val_2 = l2.val

            sum_p = val_1 + val_2 + carry

            if sum_p >= 10:
                carry = 1
                sum_p -= 10
            else:
                carry = 0
            curr.next = ListNode(sum_p, None)
            curr = curr.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy.next