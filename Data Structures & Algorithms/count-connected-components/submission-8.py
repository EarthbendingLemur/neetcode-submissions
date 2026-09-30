class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        # DFS and add to a set
        visited = set()

        def DFS(root_node):
            stack = [root_node]
            while stack:
                node = stack.pop()
                for neigh in adj[node]:
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    stack.append(neigh)
                
        
        res = 0
        for node, _ in adj.items():
            if node not in visited:
                visited.add(node)
                DFS(node)
                res += 1

        return n - len(adj) + res