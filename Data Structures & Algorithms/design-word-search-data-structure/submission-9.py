class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curNode = self.root
        for c in word:
            if c not in curNode.children:
                curNode.children[c] = TrieNode()
            curNode = curNode.children[c]

        curNode.endOfWord = True
        

    def search(self, word: str) -> bool:
        # '.' count as any letter
        # Current Node, cur_word_idx
        # DFS and return True if found
        stack = [(self.root, 0)]

        while stack:
            curNode, word_idx = stack.pop()
            if word_idx == len(word):
                if curNode.endOfWord:
                    return True
                continue
            
            for childChar, childNode in curNode.children.items():
                if word[word_idx] == '.' or word[word_idx] == childChar:
                    stack.append((childNode, word_idx + 1))

        return False
