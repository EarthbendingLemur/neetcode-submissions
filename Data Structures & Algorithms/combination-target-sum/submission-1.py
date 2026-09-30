class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # temp sol
        sol = []
        def backtrack(idx, sol, sm):
            # Base Case
            if sm == target:
                res.append(sol.copy())
                return
            # No combination found
            if idx >= len(nums) or sm > target:
                return
            
            # Include value nums[idx]
            sol.append(nums[idx])
            # idx doesnt change since we aren't limiting it
            backtrack(idx, sol, sm + nums[idx])
            # Never include nums[idx]
            sol.pop()
            backtrack(idx + 1, sol, sm)

        backtrack(0, sol, 0)

        return res
            

            

            