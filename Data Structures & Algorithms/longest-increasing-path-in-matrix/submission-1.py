class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}
        def DFS(row, col, prev) -> int:
            if (row < 0 or row == ROWS or
                col < 0 or col == COLS or matrix[row][col] <= prev):
                return 0
            
            if (row, col) in cache:
                return cache[(row, col)]

            lip = 1
            lip = max(lip, 1 + DFS(row + 1, col, matrix[row][col]))
            lip = max(lip, 1 + DFS(row - 1, col, matrix[row][col]))
            lip = max(lip, 1 + DFS(row, col + 1, matrix[row][col]))
            lip = max(lip, 1 + DFS(row, col - 1, matrix[row][col]))
        
            cache[(row, col)] = lip
            return lip



        for r in range(ROWS):
            for c in range(COLS):
                DFS(r, c, -1)
        return max(cache.values())

