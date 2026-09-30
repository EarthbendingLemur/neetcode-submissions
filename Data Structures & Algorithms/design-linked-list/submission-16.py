class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None, prev: ListNode = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next, self.tail.prev = self.tail, self.head

        self.length = 0
            

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        cur = self.head

        for _ in range(index + 1):
            cur = cur.next
        
        return cur.val

        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        prevHead = self.head.next

        self.head.next = newNode
        newNode.next = prevHead
        prevHead.prev = newNode

        newNode.prev = self.head
        self.length += 1


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        prevTail = self.tail.prev

        prevTail.next = newNode
        newNode.prev = prevTail

        newNode.next = self.tail
        self.tail.prev = newNode
        self.length += 1
                

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        elif index == 0:
            self.addAtHead(val)
            return
        
        newNode = ListNode(val)
        if index < self.length // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.length - index + 1):
                cur = cur.prev
        

        newNodeNext = cur.next
        cur.next = newNode
        newNode.prev = cur
        newNode.next = newNodeNext
        newNodeNext.prev = newNode
        self.length += 1



    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        cur = self.head

        for _ in range(index):
            cur = cur.next
        
        cur.next = cur.next.next
        cur.next.prev = cur
    
        self.length -= 1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)