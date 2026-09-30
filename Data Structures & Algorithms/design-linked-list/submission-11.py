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

        for _ in range(index):
            cur = cur.next
        
        print('get i:' + str(index), end=" ")
        self.print()
        return cur.next.val

        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        prevHead = self.head.next

        self.head.next = newNode
        newNode.next = prevHead
        prevHead.prev = newNode

        newNode.prev = self.head
        self.length += 1

        print('addHead ', end="")
        self.print()


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)

        prevTail = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail

        prevTail.next = newNode
        self.length += 1

        print('addTail ', end="")
        self.print()
                

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
        cur = self.head
        for _ in range(index):
            cur = cur.next

        newNodeNext = cur.next
        cur.next = newNode
        newNode.prev = cur
        newNode.next = newNodeNext
        newNodeNext.prev = newNode
        self.length += 1

        print('addIndx ', end="")
        self.print()


    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length:
            return

        cur = self.head

        for _ in range(index):
            cur = cur.next
        
        cur.next = cur.next.next
        cur.next.prev = cur
    
        self.length -= 1

        print('delete  ', end="")
        self.print()


    def print(self):
        cur = self.head
        print('length: ' + str(self.length) + " | ", end="")
        for _ in range(self.length):
            cur = cur.next
            print(str(cur.val) + '->', end="")
        print()
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)