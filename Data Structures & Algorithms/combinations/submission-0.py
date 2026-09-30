class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        sol = []
        def backtrack(i):
            if i > n:
                if len(sol) == k:
                    res.append(sol[:])
                return
            
            sol.append(i)
            backtrack(i + 1)
            sol.pop()
            backtrack(i + 1)
            
        backtrack(1)
        return res