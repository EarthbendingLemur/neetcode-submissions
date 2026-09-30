class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def DFS(root):
            stack = [root]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                for n in adj[node]:
                    if n in visited:
                        continue
                    stack.append(n)
        res = 0
        for i in range(n):
            if i not in visited:
                DFS(i)
                res += 1
            
        
        return res
        
