class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []


        sol = []

        def backtrack(sol, i):
            if len(sol) == k:
                res.append(sol[:])
                return
            if i > n:
                return
            
            for i in range(i + 1, n + 1):
                sol.append(i)
                backtrack(sol, i)
                sol.pop()
        backtrack([], 0)
        return res