class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if not stack or stack[-1][0] != c:
                stack.append((c, 1))
                continue
            
            if c == stack[-1][0]:
                stack.append((c, stack[-1][1] + 1))

            if stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()

    
        res = ""
        for c, _ in stack:
            res += c

        return res

