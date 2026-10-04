class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0

        num_nested = 0
        for c in s:
            if c == '(':
                num_nested += 1
            elif c == ')':
                num_nested -= 1
            
            res = max(num_nested, res)
    
        return res