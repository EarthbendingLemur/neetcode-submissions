class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            # Bound check
            if ((r, c) in visit or
                r < 0 or r == ROWS or
                c < 0 or c == COLS or heights[r][c] < prevHeight):
                return
        
            visit.add((r, c))

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                dfs(row, col, visit, heights[r][c])



        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) in atl and (r, c) in pac):
                    res.append([r, c])
        
        return res