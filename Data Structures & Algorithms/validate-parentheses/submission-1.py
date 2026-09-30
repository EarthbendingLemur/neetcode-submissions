class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ']':'[',
            ')':'(',
            '}':'{'
        }

        for p in s:
            if p not in pairs:
                stack.append(p)  # we come across an open bracket
                print(stack)
            else:
                if stack and pairs[p] == stack[-1]: # we get a closing bracket
                    stack.pop()
                else:
                    return False
                    
        return not stack

