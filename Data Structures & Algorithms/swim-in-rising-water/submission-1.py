class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        res = 0
        
        mh = [(grid[0][0], 0, 0)]
        visited = set()
        while mh:
            level, r, c = heapq.heappop(mh)
            res = max(level, res)
            if r == ROWS - 1 and c == COLS - 1:
                return res

            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nr == ROWS or
                    nc < 0 or nc == COLS or
                    (nr, nc) in visited):
                    continue
                heapq.heappush(mh, (grid[nr][nc], nr, nc))
                visited.add((nr, nc))
    
        return res