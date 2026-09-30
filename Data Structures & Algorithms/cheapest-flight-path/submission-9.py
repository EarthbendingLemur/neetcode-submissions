class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj = defaultdict(list)
        for s, d, t in flights:
            adj[s].append((d, t))
        visited = set()
        # cost to get to node, node, and num stops 
        hp = [(0, src, 0)]

        while hp:
            cost, node, stops = heapq.heappop(hp)

            if (node, stops) in visited:
                continue
            visited.add((node, stops))

            if node == dst:
                return cost

            for neigh, price in adj[node]:
                if neigh != dst and stops + 1 > k:
                    continue
                heapq.heappush(hp, (cost + price, neigh, stops + 1))
            
        return -1

