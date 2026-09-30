class Solution:
    def getMid(self, l: int,h: int) -> int:
        return (l + h) // 2

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])

        top_r, bot_r = 0, rows - 1
        mid_r = self.getMid(top_r, bot_r)

        while bot_r > top_r:
            if target < matrix[mid_r][0]:
                bot_r = mid_r - 1
            elif target > matrix[mid_r][-1]:
                top_r = mid_r + 1
            else:
                break
            mid_r = self.getMid(top_r, bot_r)
        
        l, r = 0, cols - 1

        while l <= r:
            m = self.getMid(l,r)
            if target > matrix[mid_r][m]:
                l = m + 1
            elif target < matrix[mid_r][m]:
                r = m - 1
            else:
                return True
        
        return False




