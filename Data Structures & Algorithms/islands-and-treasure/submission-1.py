class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Multi Source BFS from treasure outwards
        # Q to keep track of (row, col, level)
        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    visited.add((r, c))

        # BFS will naturally find shortest path
        while q:
            r, c, dist = q.popleft()
            grid[r][c] = dist
            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nr == ROWS or
                    nc < 0 or nc == COLS or
                    (nr, nc) in visited or
                    grid[nr][nc] == -1):
                    continue
                q.append((nr, nc, dist + 1))
                visited.add((nr, nc))
        
        

        