class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Store max-left index, height value
        stack = []
        res = 0
        for i, h in enumerate(heights):
            if not stack or stack[-1][1] <= h:
                stack.append((i, h))
                continue
            
            old_index = -1
            while stack and stack[-1][1] > h:
                old_index = stack[-1][0]
                res = max(res, stack[-1][1] * (i - old_index))
                stack.pop()
            stack.append((old_index, h))
        
        n = len(heights)
        while stack:
            idx, h = stack.pop()
            res = max(res, h * (n - idx))
            

        return res