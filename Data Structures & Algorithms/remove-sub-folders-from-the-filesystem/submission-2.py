class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertFolder(self, folder_path):
        f_arr = folder_path.split('/')
        f_arr = f_arr[1:]
        cur = self.root
        for f in f_arr:
            if f not in cur.children:
                cur.children[f] = TrieNode()
            cur = cur.children[f]
            if cur.eof:
                return
        cur.eof = True
    
    def printFolders(self):
        cur = self.root
        q = deque([(cur, "")])
        res = []
        while q:
            node, f = q.popleft()
            if node.eof:
                res.append(f)
                continue
            
            for child_char, child_node in node.children.items():
                q.append((child_node, f + "/" + child_char))
        
        return res


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        root = Trie()
        
        for f in folder:
            root.insertFolder(f)

        
        return root.printFolders()