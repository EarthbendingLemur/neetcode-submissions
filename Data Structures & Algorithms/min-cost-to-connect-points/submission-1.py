class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        point_set = set()
        for x, y in points:
            point_set.add((x, y))
        
        visited = set()
        num_coord = len(point_set)

        start = tuple(points[0])
        res = 0
        # distance, node
        minheap = [(0, start)]

        while minheap:
            distance, (x, y) = heapq.heappop(minheap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            res += distance
            if len(visited) == num_coord:
                return res
            for xn, yn in point_set:
                if (xn, yn) in visited:
                    continue
                cost = abs(x - xn) + abs(y - yn)
                heapq.heappush(minheap, (cost, (xn, yn)))
            
        

        return res

