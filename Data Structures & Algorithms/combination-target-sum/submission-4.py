class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sol = []

        def backtrack(i, sol, sm):
            if sm == target:
                res.append(sol[:])
                return
            
            if i >= len(nums) or sm > target:
                return
            
            # Include i
            sol.append(nums[i])
            backtrack(i, sol, sm + nums[i])          
            sol.pop()
            backtrack(i + 1, sol, sm)
            
        backtrack(0, sol, 0)
        return res