# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        dummy.next = curr
        l1,l2 = list1, list2

        while l1 and l2:
            val = -1
            if l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
             
            curr.next = ListNode(val)
            curr = curr.next
        
        curr.next = l1 or l2

        return dummy.next



