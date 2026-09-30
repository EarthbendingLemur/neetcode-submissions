class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        picked = [False] * len(nums)

        def backtrack(sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if not picked[i]:
                    sol.append(nums[i])
                    picked[i] = True
                    backtrack(sol)
                    sol.pop()
                    picked[i] = False
            
        

        backtrack([])
        return res

            

