class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:
            if  t not in ("+", "-", "/", "*"):
                stack.append(int(t))
                continue

            v1 = stack.pop()
            v2 = stack.pop()

            if t == "+":
                stack.append(v1 + v2)
            elif t == "-":
                stack.append(v2 - v1)
            elif t == "*":
                stack.append(v1 * v2)
            elif t == "/":
                stack.append(int(v2 / v1))
            else:
                continue


        return stack.pop()

