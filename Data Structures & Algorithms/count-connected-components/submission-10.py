class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()

        def DFS(node):
            stack = [node]
            while stack:
                n = stack.pop()
                if n in visited:
                    continue
                visited.add(n)
                for neigh in adj[n]:
                    if neigh in visited:
                        continue
                    stack.append(neigh)
                
    

        comp = 0
        for node, _ in adj.items():
            if node not in visited:
                DFS(node)
                comp += 1
        
        return n - len(adj) + comp 