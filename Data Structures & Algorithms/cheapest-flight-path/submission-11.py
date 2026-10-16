class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
      
        dist = [float('inf')] * n
        dist[src] = 0

        for i in range(k + 1):
            dist_c = dist.copy()

            for u, v, cost in flights:
                if dist[u] != float('inf'):
                    dist_c[v] = min(dist_c[v], dist[u] + cost)
            
            dist = dist_c
        
        return dist[dst] if dist[dst] != float('inf') else -1

