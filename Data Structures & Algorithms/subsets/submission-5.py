class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        
        def backtrack(idx, sol):
            if idx >= len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[idx])
            backtrack(idx + 1, sol)
            sol.pop()
            backtrack(idx + 1, sol)
        
        backtrack(0, [])
        return res