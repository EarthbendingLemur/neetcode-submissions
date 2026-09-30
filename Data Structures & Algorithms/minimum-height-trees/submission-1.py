class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        def BFS(root) -> int:
            if root not in adj:
                return 0
            q = deque()
            visited = set()
            q.append((root, 0))
            visited.add(root)
            max_depth = 0
            while q:
                node, level = q.popleft()
                max_depth = max(level, max_depth)
                for neigh in adj[node]:
                    if neigh not in visited:
                        q.append((neigh, level + 1))
                        visited.add(neigh)
            
            return max_depth

        res = []
        for i in range(n):
            height = BFS(i)
            if not res or res[0][1] == height:
                res.append((i, height))
            elif res[0][1] > height:
                res = []
                res.append((i, height))
        

        return [i for i, _ in res]