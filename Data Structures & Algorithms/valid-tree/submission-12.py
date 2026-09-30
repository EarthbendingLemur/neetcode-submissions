class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        q = deque()
        # Store node + parent
        q.append((0, -1))
        visited = set()
        visited.add(0)
        while q:
            node, parent = q.popleft()

            
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if neigh in visited:
                    return False
                
                q.append((neigh, node))
                visited.add(neigh)
        
        return True if len(visited) == n else False