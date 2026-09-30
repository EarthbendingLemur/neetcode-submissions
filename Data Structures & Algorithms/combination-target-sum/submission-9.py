class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sm = 0

        def backtrack(sm, sol, idx):
            if sm == target:
                res.append(sol[:])
                return

            if sm > target or idx >= len(nums):
                return
            
            sol.append(nums[idx])
            backtrack(sm + nums[idx], sol, idx)
            sol.pop()
            backtrack(sm, sol, idx + 1)         
            
    
        
        backtrack(0, [], 0)

        return res