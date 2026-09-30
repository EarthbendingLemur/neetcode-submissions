class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def DFS(root_r, root_c) -> (bool, int):
            stack = [(root_r, root_c)]
            visited.add((root_r, root_c))
            touches_edge = False
            enclave_size = 0
            while stack:
                r, c = stack.pop()
                if (r == 0 or r == ROWS - 1 or
                    c == 0 or c == COLS - 1):
                    touches_edge = True
                enclave_size += 1
                for dr, dc in dx:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] == 0 or
                        (row, col) in visited):
                        continue
                    stack.append((row, col))
                    visited.add((row, col))

            return touches_edge, enclave_size
        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    touches_edge, size = DFS(r, c)
                    if not touches_edge:
                        res += size
                    

        return res
                    
