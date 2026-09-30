class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for point in points:
            x = point[0]
            y = point[1]
            dist = (x**2 + y**2)

            minheap.append((dist, x, y))
        
        heapq.heapify(minheap)
        res = []

        for i in range(k):
            point = heapq.heappop(minheap)
            res.append([point[1], point[2]])

        return res