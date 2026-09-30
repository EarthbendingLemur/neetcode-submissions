class Node:
    def __init__(self,key=0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.mp = {}

        self.leastUsed = Node()
        self.mostUsed = Node()

        self.leastUsed.next = self.mostUsed
        self.mostUsed.prev = self.leastUsed

        self.capacity = capacity
        
    # update LL order when get, put called
    # Remove least used
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = node.next, node.prev

    # insert to most used
    def insert(self, node):
        prev, nxt = self.mostUsed.prev, self.mostUsed
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.mp:
            self.remove(self.mp[key])
            self.insert(self.mp[key])
            return self.mp[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            self.remove(self.mp[key])
        self.mp[key] = Node(key, value)
        self.insert(self.mp[key])

        if len(self.mp) > self.capacity:
            lru = self.leastUsed.next
            self.remove(lru)
            del self.mp[lru.key]
