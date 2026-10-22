class Solution:
    def minimumSteps(self, s: str) -> int:
        insert = 0
        res = 0
        for i, c in enumerate(s):
            if c == '0':
                res += i - insert
                insert += 1
        
        return res
