class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None] * len(nums)

        dp[0] = nums[0] 
        if len(dp) < 2:
            return dp[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])


        return dp[-1]