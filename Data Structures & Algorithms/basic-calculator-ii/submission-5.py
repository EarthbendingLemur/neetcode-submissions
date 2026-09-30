class Solution:
    def calculate(self, s: str) -> int:
        ops = {'+', '-', '*', '/'}
        
        
        def parseNum(start_idx) -> (int, int):
            end_idx = start_idx
            while end_idx < len(s) and s[end_idx].isdigit():
                end_idx += 1
            return (end_idx, int(s[start_idx:end_idx]))

        stack = []
        s_i = 0
        s = s.replace(" ", "")
        while s_i < len(s):
            if s[s_i].isdigit():
                end_idx, num = parseNum(s_i)
                stack.append(num)
                s_i = end_idx
            elif s[s_i] == '+' or s[s_i] == '-':
                stack.append(s[s_i])
                s_i += 1
            elif s[s_i] == '*':
                top_s = stack.pop()
                end_idx, num = parseNum(s_i + 1)
                stack.append(top_s * num)
                s_i = end_idx
            elif s[s_i] == '/':
                top_s = stack.pop()
                end_idx, num = parseNum(s_i + 1)
                stack.append(top_s // num)
                s_i = end_idx
            else:
                s_i += 1

        stack.reverse()
        while len(stack) > 1:
            n1 = stack.pop()
            sgn = stack.pop()
            n2 = stack.pop()

            if sgn == '+':
                stack.append(n1 + n2)
            elif sgn == '-':
                stack.append(n1 - n2)
    
        return stack[0]
                

                
                
