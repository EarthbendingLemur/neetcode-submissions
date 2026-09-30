class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtrack(num_open, num_closed, sol):
            if num_open == num_closed == n:
                res.append("".join(sol))
                return
            
            if num_open < n:
                sol.append('(')
                backtrack(num_open + 1, num_closed, sol)
                sol.pop()
            
            if num_closed < num_open:
                sol.append(')')
                backtrack(num_open, num_closed + 1, sol)
                sol.pop()
        
        backtrack(0, 0, [])
        return res