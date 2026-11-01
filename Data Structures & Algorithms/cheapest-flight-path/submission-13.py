class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
      
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(k + 1):
            dist_new = dist.copy()
            for s, d, cost in flights:
                if dist_new[s] != float('inf'):
                    dist_new[d] = min(dist_new[d], dist[s] + cost)
        
            dist = dist_new
        
        return dist[dst] if dist[dst] != float('inf') else -1