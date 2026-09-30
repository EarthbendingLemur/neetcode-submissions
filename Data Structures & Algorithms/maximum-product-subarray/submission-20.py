class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_prefix, dp_suffix = 0, 0
        res = nums[0]
        for i in range(len(nums)):
            dp_prefix = nums[i] * (dp_prefix or 1)
            dp_suffix = nums[len(nums) - 1 - i] * (dp_suffix or 1)
            res = max(res, dp_prefix, dp_suffix)
        
        return res
        