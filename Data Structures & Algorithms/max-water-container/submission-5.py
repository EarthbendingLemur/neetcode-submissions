class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        area = -1

        while l < r:
            c_area = min(heights[l], heights[r]) * (r - l)
            area = max(area, c_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return area
