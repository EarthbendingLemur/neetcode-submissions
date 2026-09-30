class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}

        def backtrack(idx, sm):
            if (idx, sm) in dp:
                return dp[(idx, sm)]

            if idx >= len(nums):
                return 1 if sm == target else 0
            
            dp[(idx, sm)] = backtrack(idx + 1, sm + nums[idx]) + backtrack(idx + 1, sm - nums[idx])
            return dp[(idx, sm)]
        
        backtrack(0, 0)

        return max(dp.values())
