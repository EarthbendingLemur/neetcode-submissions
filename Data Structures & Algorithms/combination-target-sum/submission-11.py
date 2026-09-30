class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []


        def backtrack(idx, sm, sol):
            # Reached Target
            if sm == target:
                res.append(sol[:])
                return
            # Invalid
            if idx >= len(nums) or sm > target:
                return
            
            # Go recursively down all paths where we choose this index
            sol.append(nums[idx])
            backtrack(idx, sm + nums[idx], sol)
            # Go down recursively all paths we don't choose this index
            # Combination of choose + not choose filtered out by base cases
            sol.pop()
            backtrack(idx + 1, sm, sol)
        

        backtrack(0, 0, [])
        return res