class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        sol = []


        def backtrack(i, sol, sm):
            # Edge case when sum exceeds target or past index (discard this solution)
            if sm > target or i >= len(nums):
                return
            
            if sm == target:
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            backtrack(i, sol, nums[i] + sm)
            sol.pop()
            backtrack(i + 1, sol, sm)       



        backtrack(0, sol, 0)
        return res

            

            