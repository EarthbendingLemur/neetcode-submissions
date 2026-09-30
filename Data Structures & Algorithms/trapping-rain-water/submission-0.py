class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        maxL = 0
        maxR = 0
        for i in range(1, len(height)):
            maxL = max(height[i - 1], maxL)
            r_idx = len(height) - i - 1
            maxR = max(height[r_idx + 1], maxR)
            maxLeft[i] = max(maxL, height[i - 1])
            maxRight[r_idx] = max(maxR, height[r_idx + 1])

        res = 0        
        for i in range(len(height)):
            trapped_water = min(maxLeft[i], maxRight[i]) - height[i] 
            res += trapped_water if trapped_water > 0 else 0

        return res