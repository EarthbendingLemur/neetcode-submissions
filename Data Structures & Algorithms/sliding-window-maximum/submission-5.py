class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        L, R = 0, k - 1
        mh = []
        for i in range(R + 1):
            heapq.heappush(mh, (-nums[i], i))
        res = []
        while R < len(nums):

            while not (L <= mh[0][1] <= R):
                heapq.heappop(mh)
            res.append(-(mh[0][0]))
            L += 1
            R += 1
            if R < len(nums):
                heapq.heappush(mh, (-nums[R], R))

        
        return res

