class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = j = 0
        stack = []
        while i < len(pushed) or j < len(popped):
            if not stack or stack[-1] != popped[j]:
                if i == len(pushed):
                    return False
                stack.append(pushed[i])
                i += 1
            elif j < len(popped) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                return False
        
        return True


