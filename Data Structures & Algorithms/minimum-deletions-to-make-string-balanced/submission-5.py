class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        res = 0

        for c in s:
            
            if c == 'b':
                stack.append(c)
            elif stack and stack[-1] == 'b':
                stack.pop()
                res += 1
            else:
                stack.append(c)
        
        return res

