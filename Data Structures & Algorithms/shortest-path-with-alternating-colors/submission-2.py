from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redAdj = {i: [] for i in range(n)}
        blueAdj = {i: [] for i in range(n)}
        total_edges = len(redEdges) + len(blueEdges)
        for s, d in redEdges:
            redAdj[s].append(d)
        for s, d in blueEdges:
            blueAdj[s].append(d)
        
        # Store (source, dest, colour)
        visited_edges = set()
        q = deque()
        q.append((0, 0, -1))
        res = [float('inf')] * n

        while q:
            node, dist, prevEdge = q.popleft()
            res[node] = min(res[node], dist)
            if prevEdge == 0 or prevEdge == -1:
                for nei in blueAdj[node]:
                    if (node, nei) in visited_edges:
                        continue
                    visited_edges.add((node, nei))
                    q.append((nei, dist + 1, 1))
            if prevEdge == 1 or prevEdge == -1:
                for nei in redAdj[node]:
                    if (node, nei) in visited_edges:
                        continue
                    visited_edges.add((node, nei))
                    q.append((nei, dist + 1, 0))


        for i, d in enumerate(res):
            if d == float('inf'):
                res[i] = -1
        return res