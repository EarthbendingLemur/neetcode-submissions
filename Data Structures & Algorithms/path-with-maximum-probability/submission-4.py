class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)

        for i, edge in enumerate(edges):
            adj[edge[0]].append((edge[1], succProb[i]))
            adj[edge[1]].append((edge[0], succProb[i]))
        
        
        best_prob = defaultdict(float)
        best_prob[start_node] = 1.0
        mh = [(-1.0, start_node)]

        while mh:
            prob, node = heapq.heappop(mh)
            prob = -prob 
            if node == end_node:
                return abs(prob)
            
            if prob < best_prob[node]:
                continue
            
            for neigh, edge_prob in adj[node]:
                new_prob = edge_prob * prob

                if new_prob > best_prob[neigh]:
                    best_prob[neigh] = new_prob
                    heapq.heappush(mh, (-new_prob, neigh))

        return 0.0