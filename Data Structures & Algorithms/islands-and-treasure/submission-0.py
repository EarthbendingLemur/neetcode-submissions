class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # Store as row, col, distance so far
                    q.append((r, c, 0))

        visited = set()
        while q:
            for _ in range(len(q)):
                r, c, dist = q.popleft()
                if (r, c) in visited: continue
                visited.add((r, c))
                for dr, dc in dx:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 2**31 - 1 or (row, col) in visited):
                        continue
                    q.append((row, col, dist + 1))
                    grid[row][col] = dist + 1
        

        

        
