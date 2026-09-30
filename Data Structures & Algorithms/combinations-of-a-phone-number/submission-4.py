class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        dig_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def backtrack(dig_idx, sol):
            if len(sol) == len(digits):
                res.append(sol)
                return
            
            for c in dig_map[digits[dig_idx]]:
                sol += c
                backtrack(dig_idx + 1, sol)
                sol = sol[:-1]
        

        backtrack(0, "")

        return res
            
        
            

