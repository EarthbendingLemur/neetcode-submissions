class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sol = []

        def backtrack(idx, sol, sm):
            if sm == target:
                res.append(sol[:])
                return
            if idx >= len(nums) or sm > target:
                return
            
            # Sm is less than target

            sol.append(nums[idx])
            backtrack(idx, sol, sm + nums[idx])
            sol.pop()
            backtrack(idx + 1, sol, sm)
        
        backtrack(0, [], 0)
        return res
