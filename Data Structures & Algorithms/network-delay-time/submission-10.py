class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstras but until all nodes are visited
        # Keep track of total cost 
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append((d, t))
        res = 0
        # store time taken to get to node, node in heap
        # minheap to optimise shortest path
        hp = [(0, k)]
        visited = set()
        while hp:
            time, node = heapq.heappop(hp)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time
            
            
            
            
            for nei, t in adj[node]:
                heapq.heappush(hp, (t + time, nei))
            
        
        return res if len(visited) == n else -1



        
            

