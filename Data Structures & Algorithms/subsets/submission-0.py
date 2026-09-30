class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i):
            # Reached all elements of array
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Decision to add i
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision to not add i
            subset.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res
            

            