class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        k = 0
        for c in s:
            if c != ']':
                if c.isdigit():
                    k = k * 10 + int(c)
                else:
                    if k != 0:
                        stack.append(k)
                    k = 0
                    stack.append(c)
            else:
                substr = deque()
                while stack and stack[-1] != '[':
                    substr.appendleft(stack.pop())
                # Deal with [
                stack.pop()
                multiplier = int(stack.pop())
                stack.append(multiplier * "".join(list(substr)))

        return "".join(stack)