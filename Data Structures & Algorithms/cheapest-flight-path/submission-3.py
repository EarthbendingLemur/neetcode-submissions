class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for s, d, cost in flights:
            adj[s].append((d, cost))
        
        print(adj)
        # Start at source
        # Store a heap (cost, numstops, node)
        minheap =  [(0, 0, src)]
        # BFS With Dijkstras from source outwards and limit to number of stops
        visited = set()
        while minheap:
            cost, stops, node = heapq.heappop(minheap)
            if node == dst:
                return cost

            if (node, stops) in visited:
                continue
            visited.add((node, stops))

            
            for neigh, w in adj[node]:
                if stops > k:
                    continue
                heapq.heappush(minheap, (cost + w, stops + 1, neigh))         

        return -1
