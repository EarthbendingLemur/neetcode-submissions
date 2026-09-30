class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        picked = [False] * len(nums)

        def backtrack(idx, sol):
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            if idx >= len(nums):
                return

            
            for i in range(len(nums)):
                if not picked[i]:
                    sol.append(nums[i])
                    picked[i] = True
                    backtrack(idx + 1, sol)
                    sol.pop()
                    picked[i] = False
            
        

        backtrack(0, [])
        return res

            

