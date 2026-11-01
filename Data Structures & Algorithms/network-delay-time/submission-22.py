import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        hp = [(0, k)]
        adj = {i:[] for i in range(1,n + 1)}
        for s, d, t in times:
            adj[s].append((d, t))
        res = 0
        visited = set()
        while hp:
            time, node = heapq.heappop(hp)
            if node in visited: continue
            visited.add(node)
            res = max(time, res)
            if len(visited) == n:
                return res
            
            for nei, t in adj[node]:
                heapq.heappush(hp, (t + time, nei))
        
        return -1
