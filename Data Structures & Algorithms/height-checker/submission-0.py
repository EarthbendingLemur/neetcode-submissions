class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        res = 0
        expected = heights.copy()
        expected.sort()
        print(expected)
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        
        return res