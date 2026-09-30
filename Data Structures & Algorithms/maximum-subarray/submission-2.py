class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        sm = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if sm < 0:
                sm = 0
            sm += nums[i]
            res = max(sm, res)
        
        return res