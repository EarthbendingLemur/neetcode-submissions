class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.pVal = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertWord(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.pVal += 1
        cur.endOfWord = True

    def getSum(self, word):
        cur = self.root
        res = 0
        for c in word:
            cur = cur.children[c]
            res += cur.pVal
        return res
             


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # Insert all words into the trie
        # Once all inserted, we DFS down into the trie adding up all the entries pVal values
        # Once we reach end of word we append to res the sum of the pVal values
        res = []

        trie = Trie()
        for w in words:
            trie.insertWord(w)

        for w in words:
            res.append(trie.getSum(w))

        return res

         

