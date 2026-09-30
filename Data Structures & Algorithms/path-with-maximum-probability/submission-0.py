class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        res = 1

        adj = defaultdict(list)
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))
        
        maxheap = [(-1, start_node)]
        visited = set()
        while maxheap:
            prob, node = heapq.heappop(maxheap)
            prob = abs(prob)
            if (node, prob) in visited:
                continue

            if node == end_node:
                return prob

            visited.add(node)

            for n, p in adj[node]:
                if n in visited:
                    continue
                heapq.heappush(maxheap, (-(p * prob), n))

        return 0