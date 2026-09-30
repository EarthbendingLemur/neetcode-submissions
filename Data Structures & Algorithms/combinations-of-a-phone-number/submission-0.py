class Solution(object):
    def letterCombinations(self, digits):
        mp = {
            2:'abc', 3:'def', 4:'ghi',
            5:'jkl', 6:'mno', 7:'pqrs',
            8:'tuv',9:'wxyz'
        }

        res = []
        sol = []

        def backtrack(idx):
            if idx == len(digits):
                res.append("".join(sol))
                return

            for c in mp[int(digits[idx])]:
                sol.append(c)
                backtrack(idx + 1)
                sol.pop()
        if not digits:
            return []

        backtrack(0)
        return res
            
