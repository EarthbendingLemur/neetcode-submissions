class Solution:
    def isValid(self, s: str) -> bool:
        compl = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }

        stack = []

        for p in s:
            if p in compl:
                if len(stack) == 0 or compl[p] != stack.pop(): 
                    return False
            else:
                stack.append(p)
        return len(stack) == 0