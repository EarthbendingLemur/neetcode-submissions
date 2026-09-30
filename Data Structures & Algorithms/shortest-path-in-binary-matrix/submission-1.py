class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        q = deque()
        q.append((0, 0, 1))
        if grid[0][0] == 1:
            return -1
        visited = set()
        while q:
            row, col, dist = q.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return dist
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            for dr, dc in dx:
                r, c = dr + row, dc + col
                if (r < 0 or r == ROWS or
                    c < 0 or c == COLS or
                    grid[r][c] != 0):
                    continue
                q.append((r, c, dist + 1))
        
        return -1

