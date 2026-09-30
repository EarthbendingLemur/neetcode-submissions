class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Start at Source
        # Minheap BFS Dijkstras from src to dst

        adj = defaultdict(list)
        for s, d, cost in flights:
            adj[s].append((d, cost))
        
        heap = [(0, 0, src)]
        visited = set()

        while heap:
            cost, stops, node = heapq.heappop(heap)
            # Cycle detection conditional
            if (node, stops) in visited:
                continue
            # Cheapest way to source would be present here
            if node == dst:
                return cost
            visited.add((node, stops))

            for neigh, price in adj[node]:
                if stops > k:
                    continue
                heapq.heappush(heap, (cost + price, stops + 1, neigh))
        
        return -1