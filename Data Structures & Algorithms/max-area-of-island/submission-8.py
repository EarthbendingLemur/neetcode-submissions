class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def DFS(root_r, root_c):
            stack = [(root_r, root_c)]
            visited.add((root_r, root_c))
            area = 0
            while stack:
                r, c = stack.pop()
                area += 1
                for dr, dc in dx:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1 or (row, col) in visited):
                        continue
                    stack.append((row, col))
                    visited.add((row, col))
            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = DFS(r, c)
                    res = max(area, res)
        
        return res

