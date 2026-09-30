class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        
        q = deque()
        q.append((0, -1))
        visited = set()
        visited.add(0)
        while q:
            node, par = q.popleft()

            for neigh in adj[node]:
                if neigh == par:
                    continue
                
                if neigh in visited:
                    return False
                visited.add(neigh)
                q.append((neigh, node))
        
        return True if len(visited) == n else False