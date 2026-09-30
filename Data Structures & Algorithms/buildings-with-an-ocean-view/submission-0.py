class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        res.append(len(heights) - 1)
        maxSoFar = heights[-1]
        for i in range(len(heights) - 2, -1, -1):
            if heights[i] > maxSoFar:
                res.append(i)
                maxSoFar = heights[i]
        
        return res[::-1]