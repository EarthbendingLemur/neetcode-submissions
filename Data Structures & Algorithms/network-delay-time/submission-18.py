class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append((d, t))
        
        # store the time taken to get to the node
        # store the node
        mh = [(0, k)]
        # If we encounter a node we've visited, we discard
        visited = set()
        while mh:
            time, node = heapq.heappop(mh)
            if node in visited:
                continue
            visited.add(node)
            if len(visited) == n:
                return time        
            
            for neigh, delay in adj[node]:
                heapq.heappush(mh, (time + delay, neigh))
        
        return -1


