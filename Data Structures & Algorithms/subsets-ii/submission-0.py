class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        sol = []
        nums.sort()
        def backtrack(idx):
            if idx >= len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[idx])
            backtrack(idx + 1)
            sol.pop()
            # Skip duplicate elements as its sorted
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1)


        backtrack(0)
        return res


