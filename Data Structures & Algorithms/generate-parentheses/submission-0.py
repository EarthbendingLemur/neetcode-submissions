class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        opn, cls = 0, 0
        sol = []

        def backtrack(opn, cls):
            if opn == cls == n:
                res.append("".join(sol))
                return
            

            if opn < n:
                sol.append('(')
                backtrack(opn + 1, cls)
                sol.pop()
            
            if cls < opn:
                sol.append(')')
                backtrack(opn, cls + 1)
                sol.pop()
            
        
        backtrack(0, 0)
        return res
            
            

