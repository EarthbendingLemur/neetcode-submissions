class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        visited = set()
        print(adj)
        def DFS(vertex, parent):

            stack = [(vertex, parent)]
            visited.add(vertex)
            while stack:
                v, p = stack.pop()
                
                for n in adj[v]:
                    if (n == p):
                        continue
                    if (n in visited):
                        return False
                    print(visited)
                    visited.add(n)
                    stack.append((n, v))
                    
            return True
                    

        return DFS(0, -1) and len(visited) == n