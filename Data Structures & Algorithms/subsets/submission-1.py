class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # temp sol arr
        sol = []

        def backtrack(idx):

            if idx >= len(nums):
                res.append(sol.copy())
                return
            
            # Choice to include idx in sol
            sol.append(nums[idx])
            backtrack(idx + 1)
            # Not include idx in sol
            sol.pop()
            backtrack(idx + 1)


        backtrack(0)
        return res
            