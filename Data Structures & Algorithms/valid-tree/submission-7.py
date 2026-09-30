class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        # Solve by iterating through with BFS
        # Store parent 
        # If we visit a node that isnt that node's parent
        # cycle detected and we return False

        visited = set()
        q = deque()
        # Store vertex and parent ** dont revisit parent ** 
        q.append((0, -1))
        while q:
            node, parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                q.append((neigh, node))


        return True if len(visited) == n else False