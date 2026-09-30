class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        candidates.sort()
        def backtrack(i, sol, sm):

            if sm == target:
                res.append(sol[:])
                return
            if sm > target or i >= len(candidates):
                return
            

            # Choose i
            sol.append(candidates[i])
            backtrack(i + 1 , sol, candidates[i] + sm)
            while i + 1  < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # Skip i
            sol.pop()
            backtrack(i + 1, sol, sm)
        
        backtrack(0, sol, 0)

        return res