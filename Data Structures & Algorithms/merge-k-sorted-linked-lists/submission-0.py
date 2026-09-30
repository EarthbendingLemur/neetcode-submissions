# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next =
# Wrapper for minheap functionality
class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        mh = []

        for sorted_list in lists:
            if sorted_list is not None:
                heapq.heappush(mh, NodeWrapper(sorted_list))
        
        while mh:
            node_wrapped = heapq.heappop(mh)
            cur.next = node_wrapped.node
            cur = cur.next
            
            if node_wrapped.node.next:
                heapq.heappush(mh, NodeWrapper(node_wrapped.node.next))
        
        return dummy.next