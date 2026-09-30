# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prevLeft = dummy
        curLeft = head
        for i in range(left - 1):
            prevLeft = curLeft
            curLeft = curLeft.next
        
        leftNode = curLeft
        prevIter = None
        for i in range(right - left + 1):
            tmp = curLeft.next
            curLeft.next = prevIter
            prevIter = curLeft
            curLeft = tmp

        prevLeft.next = prevIter
        leftNode.next = curLeft
        

        return dummy.next

        
            