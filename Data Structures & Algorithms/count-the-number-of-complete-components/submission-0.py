from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited_edges = set()
        visited_nodes = set()
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(root):
            num_nodes = 1
            num_edges = 0
            stack = [root]
            while stack:
                node = stack.pop()

                for nei in adj[node]:
                    if (node, nei) in visited_edges or (nei, node) in visited_edges:
                        continue
                    visited_edges.add((node, nei))

                    if nei not in visited_nodes:
                        visited_nodes.add(nei)
                        num_nodes += 1
                    stack.append(nei)
                    num_edges += 1  
            
            return num_edges == num_nodes * (num_nodes - 1) // 2

        
        res = 0
        for i in range(n):
            if i not in visited_nodes:
                res += dfs(i)
        
        return res