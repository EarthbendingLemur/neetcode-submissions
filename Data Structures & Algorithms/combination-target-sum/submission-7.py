class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        # keep track of index we are appending to sol
        # keep track of sol
        # keep track of rolling sum

        # Choose to add this index or not add index
        # Base cases depend on sum value and index value
        def backtrack(idx, sol, sm):
            # Discard this sol
            if idx >= len(nums) or sm > target:
                return
            # sol found
            if sm == target:
                res.append(sol[:])
                return

            # Choose to inc index
            sol.append(nums[idx])
            backtrack(idx, sol, nums[idx] + sm)
            # Choose to not inc this index
            sol.pop()
            backtrack(idx + 1, sol, sm)
        
        backtrack(0, sol, 0)
        return res
        

        
        

            