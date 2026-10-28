from collections import defaultdict
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}
        # Store direction False = direct path to node d from s, True = nondirect path (requires reverse)
        for s, d in connections:
            adj[s].append((d, True))
            adj[d].append((s, False))
        
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        res = 0
        while q:
            node = q.popleft()
            
            for nei, reverse in adj[node]:
                if nei in visited:
                    continue
                
                res += reverse
                q.append(nei)
                visited.add(nei)
        
        return res

