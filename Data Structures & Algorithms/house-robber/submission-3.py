class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums[0], nums[1] if len(nums) == 2 else 0)
    
        res_dp = [None] * len(nums)
        res_dp[0] = nums[0]
        res_dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
           res_dp[i] = max(nums[i] + res_dp[i - 2], res_dp[i - 1])

        return res_dp[-1]
