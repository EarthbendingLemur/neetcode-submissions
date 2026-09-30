class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(idx, sm, sol):
            if idx >= len(nums) or sm > target:
                return

            if sm == target:
                res.append(sol[:])
                return
            
        
            sol.append(nums[idx])
            backtrack(idx, sm + nums[idx], sol)
            sol.pop()
            backtrack(idx + 1, sm, sol)

        backtrack(0, 0, [])

        return res