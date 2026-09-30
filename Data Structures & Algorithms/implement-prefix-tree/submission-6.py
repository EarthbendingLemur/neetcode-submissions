class TrieNode:
    def __init__(self, val: str = ""):
        self.val = val
        self.children = []
        self.endOfWord = False
    
    def addChild(self, childVal: str):
        child = TrieNode(childVal)
        self.children.append(child)

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
            

    def insert(self, word: str) -> None:
        curNode = self.root

        for curChar in word:
            child = None

            for node in curNode.children:
                if node.val == curChar:
                    child = node
                    break
            
            if not child:
                curNode.addChild(curChar)            
                child = curNode.children[-1]

            curNode = child
        curNode.endOfWord = True

    def search(self, word: str) -> bool:
        curNode = self.root
        for curChar in word:
            child = None

            for node in curNode.children:
                if node.val == curChar:
                    child = node
                    break
                
                
            if child is None:
                return False
            curNode = child
        
        return curNode.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        
        for curChar in prefix:
            child = None

            for node in curNode.children:
                if node.val == curChar:
                    child = node
                    break
                
            if child is None:
                return False
                
            curNode = child
        
        return True

        