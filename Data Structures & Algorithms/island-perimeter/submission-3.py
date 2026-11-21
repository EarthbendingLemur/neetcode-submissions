class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stack = []
        found = False
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    stack.append((r, c))
                    visited.add((r, c))
                    found = True
                    break
            if found:
                break
        
        res = 0
        while stack:
            r, c = stack.pop()
            res += 4

            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nr == ROWS or
                    nc < 0 or nc == COLS or
                    grid[nr][nc] == 0):
                    continue
                res -= 1
                if (nr, nc) not in visited:
                    stack.append((nr, nc))
                    visited.add((nr, nc))

        return res

        
                    
        
