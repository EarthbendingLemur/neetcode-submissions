class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            difference = abs(heapq.heappop(max_heap)) - abs(heapq.heappop(max_heap))
            if difference == 0:
                continue
            heapq.heappush(max_heap, -difference)

        return abs(heapq.heappop(max_heap)) if max_heap else 0