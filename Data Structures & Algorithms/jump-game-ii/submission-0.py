class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for i in range(len(dp)):

            for k in range(1, nums[i] + 1):
                if i + k >= len(dp):
                    break
                dp[i + k] = min(dp[i + k], dp[i] + 1)
        
        return dp[-1]
