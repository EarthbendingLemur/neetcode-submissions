class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        stack = []

        for i,c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == "*":
                stars.append(i)
            else:
                if not stack and not stars:
                    return False
                if stack:
                    stack.pop()
                else:
                    stars.pop()
        
        while stack and stars:
            if stack.pop() > stars.pop():
                return False
        
        return not stack
                