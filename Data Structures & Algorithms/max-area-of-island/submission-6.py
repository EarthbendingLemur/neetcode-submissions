class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = set()
        ROWS, COLS = len(grid), len(grid[0])
        area = 0

        def DFS(root_r, root_c) -> int:
            stack = [(root_r, root_c)]
            res = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while stack:
                r, c = stack.pop()
                res += 1
                for dr, dc in directions:
                    row = r  + dr
                    col = c + dc

                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1 or (row, col) in islands):
                        continue
                    stack.append((row, col))
                    islands.add((row, col))
                    
            return res


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in islands:
                    islands.add((r, c))
                    area = max(area, DFS(r, c)) 
        return area