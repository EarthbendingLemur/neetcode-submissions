class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        hp = [(grid[0][0], 0, 0)]

        mx_level = 0
        visited = set()
        visited.add((0, 0))
        while hp:
            level, row, col = heapq.heappop(hp)
            
            mx_level = max(level, mx_level)
            if (row == ROWS - 1 and col == COLS - 1):
                break

            for dr, dc in dx:
                r, c = row + dr, col + dc
                if (r < 0 or r == ROWS or
                    c < 0 or c == COLS or
                    (r, c) in visited):
                    continue
                
                heapq.heappush(hp, (grid[r][c], r, c))
                visited.add((r, c))
        

        return mx_level