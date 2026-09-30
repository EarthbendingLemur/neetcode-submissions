class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        sol = []
        pick = [False] * len(nums)
        def backtrack():
           # When we've exhausted all values
            if len(sol) == len(nums):
                res.append(sol[:])        
                return
            
            # Unique integers so each nums[i] is unique
            for i in range(len(nums)):
                if not pick[i]:
                    sol.append(nums[i])
                    pick[i] = True
                    backtrack()
                    sol.pop()
                    pick[i] = False

        backtrack()

        return res