# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp = []
        dummy = ListNode()
        cur = dummy

        for lst in lists:
            if lst is not None:
                heapq.heappush(hp, NodeWrapper(lst))
        
        while hp:
            cur.next = heapq.heappop(hp).node
            cur = cur.next
            if cur.next:
                heapq.heappush(hp, NodeWrapper(cur.next))
        

        return dummy.next