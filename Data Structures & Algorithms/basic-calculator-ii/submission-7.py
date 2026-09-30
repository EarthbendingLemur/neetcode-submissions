class Solution:
    def calculate(self, s: str) -> int:
        
        #   O(N)
        s = s.replace(" ","")
        
        # Returns end index and integer parsed
        def parseDigit(start_idx) -> (int, int):
            cur_idx = start_idx
            res = 0
            while cur_idx < len(s) and s[cur_idx].isdigit():
                res = 10 * res + int(s[cur_idx])
                cur_idx += 1
            return cur_idx, res

        stack = []
        i = 0
        addsub_op = {'+', '-'}
        while i < len(s):
            if s[i].isdigit():
                i, number = parseDigit(i)
                stack.append(number)
            elif s[i] in addsub_op:
                stack.append(s[i])
                i += 1
            elif s[i] == '*':
                n1 = stack.pop()
                i, n2 = parseDigit(i + 1)
                stack.append(n1 * n2)
            elif s[i] == '/':
                n1 = stack.pop()
                i, n2 = parseDigit(i + 1)
                stack.append(n1 // n2)

        stack = stack[::-1]
        while len(stack) > 1:
            n1 = stack.pop()
            op = stack.pop()
            n2 = stack.pop()

            if op == '+':
                stack.append(n1 + n2)
            elif op == '-':
                stack.append(n1 - n2)


        return stack[0]


        