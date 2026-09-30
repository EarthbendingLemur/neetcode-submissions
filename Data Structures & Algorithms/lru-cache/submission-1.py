class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next, self.prev = next, prev

class LRUCache:

    def __init__(self, capacity: int):
        self.leastUsed = Node()
        self.mostUsed = Node()

        self.leastUsed.next= self.mostUsed
        self.mostUsed.prev = self.leastUsed
        
        self.cache = {}
        self.cap = capacity


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Call Remove from end of list
        self.remove(self.cache[key])
        # Call insert to put this key in front of list
        self.insert(self.cache[key])
        # Return cache value
        return self.cache[key].val



    def insert(self, node: Node):
        oldMRU = self.mostUsed.prev
        oldMRU.next = node
        self.mostUsed.prev = node
        node.prev = oldMRU
        node.next = self.mostUsed


    
    def remove(self, node):
        prevNode = node.prev
        prevNode.next = node.next
        node.next.prev = prevNode        

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return
        
        if len(self.cache) + 1 > self.cap:
            del self.cache[self.leastUsed.next.key]

            self.remove(self.leastUsed.next)

        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)



        
