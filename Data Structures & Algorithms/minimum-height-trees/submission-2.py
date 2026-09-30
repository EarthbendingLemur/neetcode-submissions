class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        edge_cnt = {}
        leaves = deque()

        for src, neigh in adj.items():
            edge_cnt[src] = len(neigh)
            if len(neigh) == 1:
                leaves.append(src)
            
        
        while leaves:
            if n <= 2:
                return list(leaves)
            # Multi source BFS
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    edge_cnt[nei] -= 1
                    if edge_cnt[nei] == 1:
                        leaves.append(nei)

        return []
        
        