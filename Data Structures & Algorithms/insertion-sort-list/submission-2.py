# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode()
        dummy.next = head
        prevInsert = dummy

        while prevInsert.next:
            minPrev = prevInsert
            minCur = prevInsert.next
            prevCur = prevInsert
            minElem = minCur
            
            while minCur:
                if minCur.val < minElem.val:
                    minPrev = prevCur
                    minElem = minCur
                prevCur = minCur
                minCur = minCur.next


            minPrev.next  = minElem.next

            minElem.next = prevInsert.next
            prevInsert.next = minElem

            prevInsert = minElem
       

        return dummy.next