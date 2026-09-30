class Solution:
    def rob(self, nums: List[int]) -> int:

        # Edge Cases
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        left_dp = [None] * (len(nums) - 1)
        right_dp = [None] * (len(nums) - 1)
        left_dp[0] = nums[0]
        right_dp[0] = nums[1]
        left_dp[1] = max(nums[1], nums[0])
        right_dp[1] = max(nums[1], nums[2])
        def robber(l_r, dp):
            for i in range(2, len(dp)):
                # max of previous val or sum of curr nums val + dp val 2 indexes behind
                dp[i] = max(dp[i - 1], nums[l_r + i] + dp[i - 2])
        
        robber(0, left_dp)
        robber(1, right_dp)

        return max(left_dp[-1], right_dp[-1])