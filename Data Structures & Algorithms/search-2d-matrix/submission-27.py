class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L_R, H_R = 0, ROWS - 1
        res_row = 0
        while L_R <= H_R:
            M_R = (L_R + H_R) // 2
            if matrix[M_R][0] <= target and matrix[M_R][-1] >= target:
                res_row = M_R
                break
            elif matrix[M_R][0] < target:
                L_R = M_R + 1
            else:
                H_R = M_R - 1
        
        L, R = 0, COLS - 1
        while L <= R:
            m = (R + L) // 2
            if matrix[res_row][m] == target:
                return True
            elif matrix[res_row][m] > target:
                R = m - 1
            else:
                L = m + 1

        return False