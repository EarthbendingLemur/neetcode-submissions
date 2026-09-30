class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        
        def backtrack(i, sol):
            if i >= len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            backtrack(i + 1, sol)
            sol.pop()
            backtrack(i + 1, sol)

        backtrack(0, [])

        return res