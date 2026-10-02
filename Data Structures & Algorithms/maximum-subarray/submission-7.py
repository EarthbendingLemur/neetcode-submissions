class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSm = nums[0]
        res = curSm

        for i in range(1,len(nums)):
            if curSm < 0:
                curSm = 0
            curSm += nums[i]
            res = max(curSm, res)
            
        
        return res