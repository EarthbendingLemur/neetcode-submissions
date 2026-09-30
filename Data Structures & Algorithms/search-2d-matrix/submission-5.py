class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        top_r = 0
        bot_r = rows - 1

        while top_r <= bot_r:
            mid_r = (top_r + bot_r) // 2
            if matrix[mid_r][0] > target:
                bot_r = mid_r - 1
            elif matrix[mid_r][-1] < target:
                top_r = mid_r + 1
            else:
                break
        
        mid_r = (top_r + bot_r) // 2

        l,r = 0 , cols - 1

        while l <= r:
            m = (l + r) // 2
            if matrix[mid_r][m] > target:
                r = m - 1
            elif matrix[mid_r][m] < target:
                l = m + 1
            else:
                return True
        
        return False




