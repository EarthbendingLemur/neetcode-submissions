class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        import math
        def dist(x, y):
            return x ** 2 + y ** 2
        
        for x, y in points:
            heapq.heappush(minheap, (dist(x, y), [x, y]))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(minheap)[1])
        

        return res