from collections import deque

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        for s, d in connections:
            adj[s].append((d, True))
            adj[d].append((s, False))
        
        # True -> Requires Reverse
        # False -> No Reverse Required

        q = deque()
        q.append(0)
        visited = {0}
        res = 0
        while q:
            node = q.popleft()
            
            for nei, rev in adj[node]:
                if nei in visited: continue
                visited.add(nei)
                q.append(nei)
                res += rev
        
        return res
