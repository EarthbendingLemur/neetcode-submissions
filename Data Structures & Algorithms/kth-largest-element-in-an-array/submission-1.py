class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for n in nums:
            maxheap.append(-n)

        heapq.heapify(maxheap)

        for i in range(k - 1):
            heapq.heappop(maxheap)
        
        return -heapq.heappop(maxheap)