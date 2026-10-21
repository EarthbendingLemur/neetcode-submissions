class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        skips = 0

        for c in num:
            
            while stack and int(c) < stack[-1] and skips < k:
                stack.pop()
                skips += 1
            stack.append(int(c))
        
        while skips < k:
            stack.pop()
            skips += 1
        
        stack = [str(i) for i in stack]
        return "".join(stack).lstrip("0") or "0"