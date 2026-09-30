class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, sol, sm):
            if sm > target or idx >= len(nums):
                return 
            
            if sm == target:
                res.append(sol[:])
                return
            
            sol.append(nums[idx])
            backtrack(idx, sol, sm + nums[idx])
            sol.pop()
            backtrack(idx + 1, sol, sm)
        
        backtrack(0, [], 0)
        return res
