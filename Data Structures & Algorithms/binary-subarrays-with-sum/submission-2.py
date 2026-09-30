class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(x):
            if x < 0: return 0

            sm = 0
            res = 0
            L = 0
            for R in range(len(nums)):
                sm += nums[R]

                while sm > x:
                    sm -= nums[L]
                    L += 1
                res += R - L + 1
            
            return res

        first_res = helper(goal)
        second_res = helper(goal - 1)

        return first_res - second_res