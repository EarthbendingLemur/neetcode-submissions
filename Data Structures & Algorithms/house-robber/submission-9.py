class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        if len(nums) < 3:
            return max(nums[0], nums[1] if len(nums) == 2 else 0)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1]