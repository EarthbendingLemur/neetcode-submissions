class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for s, d, t in times:
            adj[s].append((d, t))
        
        visited = set()
        hp = [(0, k)]
        
        while hp:
            time, node = heapq.heappop(hp)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            
            for neigh, cost in adj[node]:
                if neigh in visited:
                    continue
                heapq.heappush(hp,  (time + cost, neigh))
                       
        return -1