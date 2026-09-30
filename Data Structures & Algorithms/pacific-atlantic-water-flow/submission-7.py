class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pac = set()
        atl = set()
        # add first row to pac
        # add last row to atl
        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))
        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))
        

        def DFS(visited):
            stack = []
            for (r, c) in visited:
                stack.append((r, c))
            
            while stack:
                r, c = stack.pop()
                for dr, dc in dx:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        (row, col) in visited or
                        heights[row][col] < heights[r][c]):
                        continue
                    stack.append((row, col))
                    visited.add((row, col))
            return visited


        DFS(pac)
        DFS(atl)
        res = []
        for (r,c) in pac:
            if (r,c) in atl:    
                res.append([r, c])
        
        return res