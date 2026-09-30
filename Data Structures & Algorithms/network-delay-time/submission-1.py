class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstras but until all nodes are visited
        # Keep track of total cost 
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append((d, t))
        res = 0

        heap = [(0, k)]
        # Store (node, cost to reach node)
        visited = set()
        while heap: 
            cost, node = heapq.heappop(heap)
            if node in visited:
                continue    
            visited.add(node)
            if len(visited) == n:
                return cost
            for neigh, t in adj[node]:
                heapq.heappush(heap, (t + cost, neigh))

        return -1

            

