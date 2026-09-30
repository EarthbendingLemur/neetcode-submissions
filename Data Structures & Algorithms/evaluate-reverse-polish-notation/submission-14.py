class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
                continue
            
            if t == '+':
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif t == '-':
                val = -1 * stack.pop() + stack.pop()
                stack.append(val)
            elif t == '*':
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif t == '/':
                denom = stack.pop()
                num = stack.pop()
                val = int(num / denom)
                stack.append(val)
        print(stack)
        return stack.pop()