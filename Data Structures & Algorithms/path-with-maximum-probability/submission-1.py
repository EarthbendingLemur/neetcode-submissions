class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i, edge in enumerate(edges):
            adj[edge[0]].append((edge[1], succProb[i]))
            adj[edge[1]].append((edge[0], succProb[i]))
        
        mh = [(-1.0, start_node)]
        best_prob = 0
        edge_visited = set()
        while mh:
            prob, node = heapq.heappop(mh)
            if node == end_node:
                best_prob = min(best_prob, prob)
            
            for neigh, new_prob in adj[node]:
                if (node, neigh) in edge_visited:
                    continue
                edge_visited.add((node, neigh))
                heapq.heappush(mh, (prob * new_prob, neigh))               


        return abs(best_prob)