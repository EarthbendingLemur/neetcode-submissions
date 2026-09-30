class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        if len(nums) < 2:
            return maxSub
        sm = 0

        for n in nums:
            if sm < 0:
                sm = 0
            sm += n
            maxSub = max(sm, maxSub)
    
        return maxSub
