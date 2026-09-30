class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, h = 0, len(heights) - 1
        res = 0
        while l <= h:
            area = (h - l) * min(heights[l], heights[h])
            res = max(res, area)
            if heights[l] < heights[h]:
                l += 1
            else:
                h -= 1
        
        return res
