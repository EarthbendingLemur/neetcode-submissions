class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        point_set = set()
        for x, y in points:
            point_set.add((x, y))
        
        visited = set()
        num_coord = len(points)
        
        start = tuple(points[0])
        res = 0
        minheap = [(0, start)]

        while minheap:
            cost, (x, y) = heapq.heappop(minheap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            res += cost
            # termination condition when all nodes visited
            if len(visited) == num_coord:
                return res
            
            # Neighbours and weighted edges
            for (x_n, y_n) in point_set:
                if (x_n, y_n) in visited:
                    continue
                heapq.heappush(minheap,(abs(x - x_n) + abs(y - y_n), (x_n, y_n)))


        return res
