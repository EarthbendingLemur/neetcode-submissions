class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxh = []
        minh = []

        L = 0
        res = 0
        for R in range(len(nums)):
            heapq.heappush(maxh, (-nums[R], R))
            heapq.heappush(minh, (nums[R], R))

            while maxh[0][1] < L:
                heapq.heappop(maxh)
            
            while minh[0][1] < L:
                heapq.heappop(minh)
            
            while -maxh[0][0] - minh[0][0] > limit:
                L += 1

                while maxh[0][1] < L:
                    heapq.heappop(maxh)
            
                while minh[0][1] < L:
                    heapq.heappop(minh)
            
            res = max(res, R - L + 1)

        
        return res

            
            