class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)


        for i, [a, b] in enumerate(equations):
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        
        def DFS(src, dest):
            stack = [(src, 1.0)]
            visited = set()
            visited.add(src)

            while stack:
                node, val = stack.pop()
                if node == dest:
                    return val
                
                for neigh, cost in adj[node]:
                    if neigh not in visited:
                        stack.append((neigh, val * cost))
                        visited.add(neigh)
                
            return -1.0

        res = []
        for src, dest in queries:
            if src not in adj or dest not in adj:
                res.append(-1.0)
            else:
                res.append(DFS(src, dest))
        return res