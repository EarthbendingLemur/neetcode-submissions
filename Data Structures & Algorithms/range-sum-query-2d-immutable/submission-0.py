class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.pref_arr = [[0] * COLS for _ in range(ROWS)]
        for r in range(ROWS):
            prefix_rowwise = 0
            for c in range(COLS):
                prefix_rowwise += matrix[r][c]
                above_prefix = 0
                if r > 0:
                    above_prefix = self.pref_arr[r - 1][c]
                self.pref_arr[r][c] = prefix_rowwise + above_prefix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole_sq = self.pref_arr[row2][col2]
        diag_pref = 0
        if row1 > 0 and col1 > 0:
            diag_pref = self.pref_arr[row1 - 1][col1 - 1]

        above_pref = 0
        if row1 > 0:
            above_pref = self.pref_arr[row1 - 1][col2]
        left_pref = 0
        if col1 > 0:
            left_pref = self.pref_arr[row2][col1 - 1]

        return whole_sq + diag_pref - above_pref - left_pref
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)  