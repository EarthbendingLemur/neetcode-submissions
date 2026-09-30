class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, h = 0, len(heights) - 1

        max_area = 0

        while l <= h:
            area = (h - l) * min(heights[l], heights[h])
            max_area = max(area, max_area)
            if heights[l] < heights[h]:
                l += 1
            else:
                h -= 1
        
        return max_area