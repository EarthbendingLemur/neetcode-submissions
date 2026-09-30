class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_h = [-n for n in nums]

        heapq.heapify(max_h)

        for i in range(k - 1):
            heapq.heappop(max_h)

        return -heapq.heappop(max_h)