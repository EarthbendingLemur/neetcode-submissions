class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        heap = []

        for n in nums:
            heapq.heappush(heap, n)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap))

        return res