class ListNode:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev
        self.value = val


class LRUCache:



    def __init__(self, capacity: int):
        self.mp = {}
        self.capacity = capacity
        self.size = 0
        self.leastUsed = ListNode(-1,0)
        self.mostUsed = ListNode(-1,0)

        self.leastUsed.next = self.mostUsed
        self.mostUsed.prev = self.leastUsed

    def get(self, key: int) -> int:
        # Remove from its cur position
        # Insert into most recently used position
        # Return value from mp
        if key not in self.mp:
            return -1
        val = self.mp[key].value

        self.remove(key)
        self.insert(key, val)

        return self.mp[key].value

    

    def insert(self, key: int, value: int):
        prevUsed = self.mostUsed.prev
        curNode = ListNode(key, value)

        self.mostUsed.prev = curNode
        curNode.prev = prevUsed
        curNode.next = self.mostUsed
        prevUsed.next = curNode

        self.mp[curNode.key] = curNode
        self.size += 1
    


    def remove(self, key: int):
        curNode = self.mp[key]
        prevNode = curNode.prev
        prevNode.next = curNode.next
        curNode.next.prev = prevNode
        self.size -= 1
        del self.mp[key]



    def put(self, key: int, value: int) -> None:
        # Remove from its cur position if exists
        # insert into most recently used
        # Check capacity and eject least recently used

        if key in self.mp:
            self.remove(key)
            self.insert(key, value)
            return
        
        if self.size + 1 > self.capacity:
            self.remove(self.leastUsed.next.key)

        self.insert(key, value)

        
