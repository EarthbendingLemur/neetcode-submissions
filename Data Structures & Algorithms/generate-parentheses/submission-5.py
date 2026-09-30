class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(num_closed, num_open, sol):
            if num_closed == num_open == n:
                res.append(('').join(sol))
                return
            
            if num_open < n:
                sol.append('(')
                backtrack(num_closed, num_open + 1, sol)
                sol.pop()
    
            
            if num_closed < num_open:
                sol.append(')')
                backtrack(num_closed + 1, num_open, sol)
                sol.pop()


        backtrack(0, 0, [])
        return res
            
        