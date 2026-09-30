class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        L, R = 0, len(heights) - 1


        while L < R:
            area = min(heights[L], heights[R]) * (R - L)
            res = max(area, res)
            if heights[L] > heights[R]:
                R -= 1
            else:
                L += 1



        return res