class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])
        
        visited = set()
        def DFS(v):
            stack = [v]

            while stack:
                vertex = stack.pop()
                for neigh in adj[vertex]:
                    if neigh in visited:
                        continue
                    stack.append(neigh)
                    visited.add(neigh)
                

        
        num_comp = 0
        
        for node, _ in adj.items():
            if node not in visited:
                num_comp += 1
                visited.add(node)
                DFS(node)


        return n - len(adj) + num_comp