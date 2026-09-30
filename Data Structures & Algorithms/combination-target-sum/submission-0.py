class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total):
            # Base Case - Reached Target
            if total == target:
                res.append(cur.copy())
                return
            # Combination 404
            if i >= len(nums) or total > target:
                return
            
            # Include nums[i] in d-tree
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])
            cur.pop() 

            # Not include nums[i] in d-tree (Have to inc i + 1)
            backtrack(i + 1, cur, total)
        
        backtrack(0, [], 0)

        return res

            

            

            