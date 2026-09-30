class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        stack = []

        # initialise stack and find starting island for DFS
        found_start = False
        for r in range(ROWS):
            if found_start:
                break
            for c in range(COLS):
                if grid[r][c] == 1:
                    stack.append((r, c))
                    visited.add((r, c))
                    found_start = True
                    break
        
        res = 0
        directions =[(1, 0), (-1, 0), (0, 1), (0, -1)]
        while stack:
            node_r, node_c = stack.pop()

            num_neigh = 0
            for dr, dc in directions:
                row  = dr + node_r
                col = dc + node_c
                if (row < 0 or row == ROWS or
                    col < 0 or col == COLS or grid[row][col] != 1):
                    continue
                if (row, col) not in visited:
                    visited.add((row, col))
                    stack.append((row, col))
                num_neigh += 1
            res += 4 - num_neigh
        return res
        
