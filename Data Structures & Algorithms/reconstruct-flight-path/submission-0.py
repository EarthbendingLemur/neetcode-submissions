class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)
        for src, dest in tickets:
            heapq.heappush(adj[src], dest)
        
        path = []
        stack = ["JFK"]
        while stack:
            cur = stack[-1]

            if adj[cur]:
                dest = heapq.heappop(adj[cur])
                stack.append(dest)
            else:
                path.append(stack.pop())
                
        return path[::-1]
        