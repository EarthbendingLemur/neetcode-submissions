class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curSm, sol):
            if i >= len(nums) or curSm > target:
                return
            
            if curSm == target:
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            dfs(i, curSm + nums[i], sol)
            sol.pop()
            dfs(i + 1, curSm, sol)
        
        dfs(0, 0, [])
        return res