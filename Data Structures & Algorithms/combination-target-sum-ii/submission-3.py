class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(idx, sol, sm):
            if sm == target:
                res.append(sol[:])
                return
            if sm > target or idx >= len(candidates):
                return
            
            sol.append(candidates[idx])
            backtrack(idx + 1, sol, candidates[idx] + sm)
            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            sol.pop()
            backtrack(idx + 1, sol, sm)
        
        backtrack(0, [], 0)
        return res