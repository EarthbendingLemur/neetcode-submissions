class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        L, R = 0, k - 1

        window = []
        for i in range(k):
            heapq.heappush(window, (-nums[i], i))
        
        output = []
        while R < len(nums):
            while not (L <= window[0][1] <= R):
                heapq.heappop(window)
            
            output.append(-(window[0][0]))
            R += 1
            L += 1
            if R < len(nums):
                heapq.heappush(window, (-nums[R], R))
        
        return output
        
            





