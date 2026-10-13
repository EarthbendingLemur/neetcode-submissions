class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = []

        for n in nums:
            if len(hp) < k:
                heapq.heappush(hp, n)
                continue
            
            if n < hp[0]:
                continue
            heapq.heappop(hp)
            heapq.heappush(hp, n)
        
        return hp[0]
            
            