class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        res = []
        for c in s:
            if not stack and c != '(':
                res.append(c)
                continue
            
            if c != ')':
                stack.append(c)
            else:
                sub = []
                while stack and stack[-1] != '(':
                    sub.append(stack.pop())
                stack.pop()
                if not stack:
                    res.extend(sub)
                else:
                    stack.extend(sub)

        return "".join(res)
