class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visit):
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        (row, col) in visit or
                        heights[row][col] <  heights[r][c]):
                        continue   
                    visit.add((row, col))
                    stack.append((row, col))


        # DFS for all RO EDGES
        for c in range(COLS):
            pac.add((0, c))
            dfs(0, c, pac)
            atl.add((ROWS - 1, c))
            dfs(ROWS - 1, c, atl)
        
        # DFS for all COL EDGES
        for r in range(ROWS):
            pac.add((r, 0))
            dfs(r, 0, pac)
            atl.add((r, COLS - 1))
            dfs(r, COLS - 1, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if ((r, c) in atl and (r, c) in pac):
                    res.append([r, c])
        
        return res