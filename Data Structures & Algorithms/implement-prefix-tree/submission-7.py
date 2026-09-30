class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
                

    def insert(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()

            curNode = curNode.children[c]
        # Mark as end of word
        curNode.endOfWord = True

        


    def search(self, word: str) -> bool:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        
        return curNode.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for c in prefix:
            if c not in curNode.children:
                return False
            curNode = curNode.children[c]
        
        return True
        
        